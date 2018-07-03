"""empty message

Revision ID: b5a37c22a880
Revises: 3c6348959b63
Create Date: 2018-07-03 17:45:23.034755

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5a37c22a880'
down_revision = '3c6348959b63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movies', sa.Column('extra', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movies', 'extra')
    # ### end Alembic commands ###
