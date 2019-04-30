"""Fourth Migration-Add Comment Model

Revision ID: 3233b2b8e1eb
Revises: cc2448ac457c
Create Date: 2019-04-28 21:36:59.465209

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3233b2b8e1eb'
down_revision = 'cc2448ac457c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=255), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('blogger_id', sa.Integer(), nullable=True),
    sa.Column('visitor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blogger_id'], ['bloggers.id'], ),
    sa.ForeignKeyConstraint(['visitor_id'], ['visitors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('visitors', 'posted')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('visitors', sa.Column('posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_table('comments')
    # ### end Alembic commands ###