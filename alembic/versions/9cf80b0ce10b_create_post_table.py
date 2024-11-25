"""Create Post Table

Revision ID: 9cf80b0ce10b
Revises: 47ed45348b7d
Create Date: 2024-11-24 15:05:19.516692

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9cf80b0ce10b'
down_revision: Union[str, None] = '47ed45348b7d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
