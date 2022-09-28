"""create users table

Revision ID: fd6549486548
Revises: 
Create Date: 2022-09-28 20:29:25.633518

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd6549486548'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('user_id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('email', sa.String(length=50), nullable=False),
                    sa.Column('password', sa.String(
                        length=50), nullable=False),
                    sa.Column('username', sa.String(
                        length=50), nullable=False),
                    sa.Column('surname', sa.String(length=50), nullable=False),
                    sa.Column('blocked', sa.Boolean(), nullable=False),
                    sa.PrimaryKeyConstraint('user_id')
                    )


def downgrade() -> None:
    op.drop_table('users')
