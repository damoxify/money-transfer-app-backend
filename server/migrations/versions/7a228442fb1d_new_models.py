"""new models

Revision ID: 7a228442fb1d
Revises: 
Create Date: 2024-01-10 09:22:42.564490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a228442fb1d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('fullname', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('digital_signature', sa.String(length=255), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('beneficiaries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('account_number', sa.Integer(), nullable=True),
    sa.Column('bank', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_beneficiaries_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wallet_accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('balance', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_wallet_accounts_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('narration', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('beneficiary_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['beneficiary_id'], ['beneficiaries.id'], name=op.f('fk_transactions_beneficiary_id_beneficiaries')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_transactions_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.drop_table('wallet_accounts')
    op.drop_table('beneficiaries')
    op.drop_table('users')
    # ### end Alembic commands ###
