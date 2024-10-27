"""add index to tittle and content

Revision ID: 1427714cf6dc
Revises: 5c0269b50e0e
Create Date: 2024-10-27 15:50:57.766048

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1427714cf6dc'
down_revision: Union[str, None] = '5c0269b50e0e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.create_index('idx_title_content', 'posts', ['title', 'content'])

def downgrade():
    op.drop_index('idx_title_content', table_name='posts')
