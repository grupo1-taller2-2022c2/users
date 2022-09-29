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
                       {'email': 'agus_su@gmail.com', 'password': '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4',
                        'username': 'agusmujer', 'surname': "su", 'blocked': False},
                       {'email': 'chino@hotmail.com', 'password': '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4',
                        'username': 'chino', 'surname': "g", 'blocked': False},
                       {'email': 'mati@yahoo.com', 'password': '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4',
                        'username': 'mati', 'surname': "matii", 'blocked': False},
                       {'email': 'juani@gmail.com', 'password': '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4',
                        'username': 'juani', 'surname': "blabla", 'blocked': False},
                       {'email': 'cristo@gmail.com', 'password': '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'username': 'cristo', 'surname': "apellido", 'blocked': False}])


def downgrade() -> None:
    pass
