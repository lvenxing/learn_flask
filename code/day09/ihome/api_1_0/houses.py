# coding:utf-8

from . import api
from ihome.models import Area
from flask import current_app, jsonify
from ihome.utils.response_code import RET
from ihome import redis_store, constants
import json


@api.route("/areas")
def get_area_info():
    """获取城区信息"""
    # 先尝试从redis中获取缓存数据
    try:
        areas_json = redis_store.get("area_info")
    except Exception as e:
        current_app.logger.error(e)
        areas_json = None

    if areas_json is None:
        # 查询数据库，获取城区信息
        try:
            areas_list = Area.query.all()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg="查询城区信息异常")

        # 遍历列表，处理每一个对象，转换一下对象的属性名
        areas = []
        for area in areas_list:
            areas.append(area.to_dict())

        # 将数据转换为json
        areas_json = json.dumps(areas)
        # 将数据在redis中保存一份缓存
        try:
            redis_store.setex("area_info", constants.AREA_INFO_REDIS_EXPIRES, areas_json)
        except Exception as e:
            current_app.logger.error(e)
    else:
        # 表示redis中有缓存，直接使用的是缓存数据
        current_app.logger.info("hit redis cache area info")

    # 从redis中去取的json数据或者从数据库中查询并转为的json数据
    # areas_json = '[{"aid":xx, "aname":xxx}, {},{}]'

    return '{"errno": 0, "errmsg": "查询城区信息成功", "data":{"areas": %s}}' % areas_json, 200, \
           {"Content-Type": "application/json"}

