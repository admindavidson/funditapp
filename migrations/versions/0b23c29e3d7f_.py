"""empty message

Revision ID: 0b23c29e3d7f
Revises: 3eeef3d6e0b7
Create Date: 2024-03-03 11:50:42.571969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b23c29e3d7f'
down_revision = '3eeef3d6e0b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('admin', schema=None) as batch_op:
        batch_op.drop_constraint('admin_ibfk_1', type_='foreignkey')
        batch_op.create_foreign_key(None, 'user', ['admin_userid'], ['user_id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('admin', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('admin_ibfk_1', 'user', ['admin_userid'], ['user_id'])

    # ### end Alembic commands ###
