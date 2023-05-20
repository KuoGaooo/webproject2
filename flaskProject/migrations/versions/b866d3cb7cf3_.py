"""empty message

Revision ID: b866d3cb7cf3
Revises: 02ff8a049133
Create Date: 2023-05-20 22:12:02.526638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b866d3cb7cf3'
down_revision = '02ff8a049133'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('email_captcha', schema=None) as batch_op:
        batch_op.drop_index('email')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('email_captcha', schema=None) as batch_op:
        batch_op.create_index('email', ['email'], unique=False)

    # ### end Alembic commands ###