"""Third Migration

Revision ID: 77c1c6624d4f
Revises: 2a0c38a26862
Create Date: 2017-11-01 08:18:49.256215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77c1c6624d4f'
down_revision = '2a0c38a26862'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment_section_id', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pitches_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitches_id'], ['pitches.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    # ### end Alembic commands ###
