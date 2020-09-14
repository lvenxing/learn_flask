# coding:utf-8


from flask import Flask, request, abort
import hashlib
import xmltodict
import time

app = Flask(__name__)

WECHAT_TOKEN = "itcast"


@app.route("/wechat8000", methods=["GET", "POST"])
def wechat():
    """对接微信服务器"""
    # 获取参数
    signature = request.args.get("signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")
    echostr = request.args.get("echostr")

    # 进行参数计算
    # 1. 进行排序
    li = [WECHAT_TOKEN, timestamp, nonce]
    li.sort()
    # 2. 拼接成字符串
    tmp_str = "".join(li)
    # 3. 进行sha1加密
    sign = hashlib.sha1(tmp_str).hexdigest()

    if signature != sign:
        # 表示不是微信发送过来里的请求， 拒绝
        abort(403)
    else:
        # 如果与微信传过来的参数相匹配，则返回echostr
        if request.method == "GET":
            # 表示是微信初始接入时发的GET请求
            return echostr
        else:
            # post请求方式，表示微信将用户的消息转发过来
            # 接收消息
            req_xml = request.data
            req_dict = xmltodict.parse(req_xml)
            req_dict = req_dict["xml"]
            # 获取消息类型
            msg_type = req_dict.get("MsgType")
            if msg_type == "text":
                # 表示文本类型消息
                # 构建返回的字典数据
                resp_dict = {
                    "ToUserName": req_dict.get("FromUserName"),
                    "FromUserName": req_dict.get("ToUserName"),
                    "CreateTime": int(time.time()),
                    "MsgType": "text",
                    "Content": req_dict.get("Content")
                }
            elif msg_type == "voice":
                # 语音类型
                resp_dict = {
                    "ToUserName": req_dict.get("FromUserName"),
                    "FromUserName": req_dict.get("ToUserName"),
                    "CreateTime": int(time.time()),
                    "MsgType": "text",
                    "Content": req_dict.get("Recognition")
                }
            elif "event" == msg_type:
                if "subscribe" == req_dict.get("Event"):
                    resp_dict = {
                        "ToUserName": req_dict.get("FromUserName", ""),
                        "FromUserName": req_dict.get("ToUserName", ""),
                        "CreateTime": int(time.time()),
                        "MsgType": "text",
                        "Content": u"感谢您的关注！"
                    }
                    if None != req_dict.get("EventKey"):
                        resp_dict["Content"] += u"场景值:"
                        resp_dict["Content"] += req_dict.get("EventKey")[8:]
                elif "SCAN" == req_dict.get("Event"):
                    resp_dict = {
                        "ToUserName": req_dict.get("FromUserName", ""),
                        "FromUserName": req_dict.get("ToUserName", ""),
                        "CreateTime": int(time.time()),
                        "MsgType": "text",
                        "Content": u"您扫描的场景值为：%s" % req_dict.get("EventKey")
                    }
            else:
                resp_dict = {
                    "ToUserName": req_dict.get("FromUserName"),
                    "FromUserName": req_dict.get("ToUserName"),
                    "CreateTime": int(time.time()),
                    "MsgType": "text",
                    "Content": "i love u"
                }

            resp_dict = {"xml": resp_dict}
            return xmltodict.unparse(resp_dict)

#
# {
#     "xml": {
#         "ToUserName": "xxxx",
#         "FromUserName": "xxxx",
#         ...
#
#     }
# }



if __name__ == '__main__':
    app.run(port=8000)