"""Second Migration-BlogPost

Revision ID: cec018fa9ebc
Revises: 349e467dc8d3
Create Date: 2019-04-27 22:22:03.876053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cec018fa9ebc'
down_revision = '349e467dc8d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogposts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('content', sa.String(length=255), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('blogpost_pic_path', sa.String(), nullable=True),
    sa.Column('blogger_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blogger_id'], ['bloggers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_bloggers_email'), 'bloggers', ['email'], unique=True)
    op.create_index(op.f('ix_bloggers_username'), 'bloggers', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_bloggers_username'), table_name='bloggers')
    op.drop_index(op.f('ix_bloggers_email'), table_name='bloggers')
    op.drop_table('blogposts')
    # ### end Alembic commands ###