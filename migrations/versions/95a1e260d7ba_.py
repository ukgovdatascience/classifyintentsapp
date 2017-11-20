"""empty message

Revision ID: 95a1e260d7ba
Revises: 7b6db31373a3
Create Date: 2017-10-19 14:26:36.059746

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95a1e260d7ba'
down_revision = '7b6db31373a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'location')
    op.drop_column('users', 'about_me')
    op.drop_column('users', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('about_me', sa.TEXT(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('location', sa.VARCHAR(length=64), autoincrement=False, nullable=True))
    # ### end Alembic commands ###