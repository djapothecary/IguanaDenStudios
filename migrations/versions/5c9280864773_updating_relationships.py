"""updating relationships

Revision ID: 5c9280864773
Revises: c901587bea6a
Create Date: 2019-03-22 16:36:25.341974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c9280864773'
down_revision = 'c901587bea6a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tracklist_details', type_='foreignkey')
    op.create_foreign_key(None, 'tracklist_details', 'tracklist_names', ['tracklist_name_id'], ['artist_dj_name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tracklist_details', type_='foreignkey')
    op.create_foreign_key(None, 'tracklist_details', 'tracklist_names', ['tracklist_name_id'], ['id'])
    # ### end Alembic commands ###
