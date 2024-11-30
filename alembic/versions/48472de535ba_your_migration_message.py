"""Your migration message

Revision ID: 48472de535ba
Revises: cbb1915636f8
Create Date: 2024-11-29 02:32:05.532940

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision: str = '48472de535ba'
down_revision: Union[str, None] = 'cbb1915636f8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def table_exists(table_name):
    bind = op.get_bind()
    inspector = Inspector.from_engine(bind)
    return table_name in inspector.get_table_names()

def upgrade():
    if not table_exists("profiles"):
        op.create_table(
            'profiles',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('first_name', sa.String(40)),
            sa.Column('last_name', sa.String(40)),
            sa.Column('bio', sa.String),
            sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False, unique=True),
        )

def downgrade():
    op.drop_table('profiles')

