"""create users table

Revision ID: 2123cddac465
Revises: 
Create Date: 2022-09-28 05:02:17.105912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2123cddac465'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=True),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
