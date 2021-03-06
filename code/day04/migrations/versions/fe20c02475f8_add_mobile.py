"""add mobile

Revision ID: fe20c02475f8
Revises: ee602d992e79
Create Date: 2017-11-02 15:08:17.727897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe20c02475f8'
down_revision = 'ee602d992e79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tbl_authors', sa.Column('mobile', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tbl_authors', 'mobile')
    # ### end Alembic commands ###
