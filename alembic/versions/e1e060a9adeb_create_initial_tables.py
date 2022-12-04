"""create initial tables

Revision ID: e1e060a9adeb
Revises: 
Create Date: 2022-09-28 21:04:55.731417

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e1e060a9adeb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('addresses',
                    sa.Column('user_id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('street_name', sa.String(
                        length=50), nullable=False),
                    sa.Column('street_number', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('user_id')
                    )
    op.create_table('drivers',
                    sa.Column('user_id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('ratings', sa.Integer(), nullable=False),
                    sa.Column('state', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('user_id')
                    )
    op.create_table('passengers',
                    sa.Column('user_id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('ratings', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('user_id')
                    )
    global users
    users = op.create_table('users',
                            sa.Column('user_id', sa.Integer(),
                                      autoincrement=True, nullable=False),
                            sa.Column('email', sa.String(
                                length=50), nullable=False),
                            sa.Column('password', sa.String(length=100),
                                      nullable=False),
                            sa.Column('username', sa.String(
                                length=50), nullable=False),
                            sa.Column('surname', sa.String(
                                length=50), nullable=False),
                            sa.Column('blocked', sa.Boolean(), nullable=False),
                            sa.Column('photo', sa.String(length=150), nullable=True),
                            sa.PrimaryKeyConstraint('user_id')
                            )
    op.create_table('vehicles',
                    sa.Column('user_id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('licence_plate', sa.String(), nullable=False),
                    sa.Column('model', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('user_id')
                    )


def downgrade() -> None:
    op.drop_table('vehicles')
    op.drop_table('users')
    op.drop_table('passengers')
    op.drop_table('drivers')
    op.drop_table('addresses')
