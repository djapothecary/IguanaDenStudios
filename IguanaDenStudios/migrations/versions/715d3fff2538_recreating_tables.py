"""recreating tables

Revision ID: 715d3fff2538
Revises: 
Create Date: 2019-03-06 12:25:45.643868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '715d3fff2538'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tracklist_name',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_dj_name', sa.String(), nullable=True),
    sa.Column('tracklist_mix_name', sa.String(), nullable=True),
    sa.Column('upload_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('tracklist_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('track_artist', sa.String(), nullable=True),
    sa.Column('track_title', sa.String(), nullable=True),
    sa.Column('tracklist_name_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['tracklist_name_id'], ['tracklist_name.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tracklist_details')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('tracklist_name')
    # ### end Alembic commands ###
