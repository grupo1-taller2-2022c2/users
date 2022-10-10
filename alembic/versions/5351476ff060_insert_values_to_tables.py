"""insert values to tables

Revision ID: 5351476ff060
Revises: e1e060a9adeb
Create Date: 2022-09-28 21:42:12.498364

"""
from app.models import users_models, passengers_models, drivers_models
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5351476ff060'
down_revision = 'e1e060a9adeb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.bulk_insert(users_models.User.__table__,
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

    op.bulk_insert(passengers_models.Passenger.__table__,
                   [
                       {'user_id': 1, 'ratings': 4},
                       {'user_id': 2, 'ratings': 2},
                       {'user_id': 3, 'ratings': 3},
                       {'user_id': 4, 'ratings': 4},
                       {'user_id': 5, 'ratings': 5}])

    op.bulk_insert(passengers_models.Address.__table__,
                   [
                       {'user_id': 1, 'street_name': 'Salta', 'street_number': 1200},
                       {'user_id': 2, 'street_name': 'Jujuy', 'street_number': 2200},
                       {'user_id': 3, 'street_name': 'Formosa',
                           'street_number': 3300},
                       {'user_id': 4, 'street_name': 'Catamarca',
                           'street_number': 5400},
                       {'user_id': 5, 'street_name': 'Cordoba', 'street_number': 9100}])

    op.bulk_insert(drivers_models.Driver.__table__,
                   [
                       {'user_id': 2, 'ratings': 4},
                       {'user_id': 5, 'ratings': 3}])

    op.bulk_insert(drivers_models.Vehicle.__table__,
                   [
                       {'user_id': 2, 'licence_plate': 'AA314CC',
                           'model': 'Ford Mustang'},
                       {'user_id': 5, 'licence_plate': 'BA341DE', 'model': 'Fitito'}])


def downgrade() -> None:
    pass
