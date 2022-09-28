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
    users = op.create_table('users',
                            sa.Column('email', sa.String(
                                length=50), nullable=False),
                            sa.Column('password', sa.String(
                                length=50), nullable=True),
                            sa.PrimaryKeyConstraint('email')
                            )

    op.bulk_insert(users,
                   [
                       {'email': 'agus_su@gmail.com', 'password': '123'},
                       {'email': 'chino@hotmail.com', 'password': '1234'},
                       {'email': 'mati@yahoo.com', 'password': '1235'},
                       {'email': 'juani@gmail.com', 'password': '1236'},
                       {'email': 'cristo@gmail.com', 'password': '1237'}])


def downgrade() -> None:
    op.drop_table('users')
