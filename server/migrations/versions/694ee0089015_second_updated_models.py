"""second updated models

Revision ID: 694ee0089015
Revises: 7a228442fb1d
Create Date: 2024-01-10 16:46:17.066437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '694ee0089015'
down_revision = '7a228442fb1d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_authenticated', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_authenticated')
    # ### end Alembic commands ###