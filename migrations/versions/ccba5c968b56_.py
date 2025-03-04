"""empty message

Revision ID: ccba5c968b56
Revises: b92c25d33093
Create Date: 2023-11-25 23:22:23.987125

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ccba5c968b56'
down_revision = 'b92c25d33093'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('website_link', sa.String(length=120), nullable=True))
    op.alter_column('artists', 'genres',
               existing_type=postgresql.ARRAY(sa.VARCHAR()),
               nullable=False)
    op.drop_column('artists', 'website')
    op.alter_column('venues', 'genres',
               existing_type=postgresql.ARRAY(sa.VARCHAR()),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venues', 'genres',
               existing_type=postgresql.ARRAY(sa.VARCHAR()),
               nullable=True)
    op.add_column('artists', sa.Column('website', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.alter_column('artists', 'genres',
               existing_type=postgresql.ARRAY(sa.VARCHAR()),
               nullable=True)
    op.drop_column('artists', 'website_link')
    # ### end Alembic commands ###
