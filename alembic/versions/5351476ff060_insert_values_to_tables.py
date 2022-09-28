"""insert values to tables

Revision ID: 5351476ff060
Revises: e1e060a9adeb
Create Date: 2022-09-28 21:42:12.498364

"""
from app.models.users_models import User
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5351476ff060'
down_revision = 'e1e060a9adeb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.bulk_insert(User.__table__,
                   [
                       {'email': 'agus_su@gmail.com', 'password': '123',
                        'username': 'pepe', 'surname': "pepo", 'blocked': False},
                       {'email': 'chino@hotmail.com', 'password': '1234',
                        'username': 'pepe', 'surname': "pepo", 'blocked': False},
                       {'email': 'mati@yahoo.com', 'password': '1235',
                        'username': 'pepe', 'surname': "pepo", 'blocked': False},
                       {'email': 'juani@gmail.com', 'password': '1236',
                        'username': 'pepe', 'surname': "pepo", 'blocked': False},
                       {'email': 'cristo@gmail.com', 'password': '1237', 'username': 'pepe', 'surname': "pepo", 'blocked': False}])


def downgrade() -> None:
    pass
