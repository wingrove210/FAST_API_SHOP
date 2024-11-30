"""empty message

Revision ID: 03fb9940ba4f
Revises: aba9e2ecaa31, def24f23dea2
Create Date: 2024-11-30 03:49:28.494043

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '03fb9940ba4f'
down_revision: Union[str, None] = ('aba9e2ecaa31', 'def24f23dea2')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
