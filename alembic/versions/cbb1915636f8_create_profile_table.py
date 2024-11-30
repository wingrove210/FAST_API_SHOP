from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


revision = 'cbb1915636f8'
down_revision = '66a7b2f44e4a'
branch_labels = None
depends_on = None
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
