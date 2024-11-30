"""Your migration message

Revision ID: c9f86592b1c3
Revises: 48472de535ba
Create Date: 2024-11-29 02:37:12.200863

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9f86592b1c3'
down_revision: Union[str, None] = '48472de535ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
