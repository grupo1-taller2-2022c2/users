"""photo_added_to_users

Revision ID: 7f2d031ce43d
Revises: bbe7b1a288a7
Create Date: 2022-12-04 22:34:59.215713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7f2d031ce43d"
down_revision = "bbe7b1a288a7"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("photo", sa.String(length=150), nullable=True))


def downgrade() -> None:
    op.drop_column("users", "photo")
