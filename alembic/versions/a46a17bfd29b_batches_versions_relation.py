"""batches_versions_relation

Revision ID: a46a17bfd29b
Revises: a31c98c74ea0
Create Date: 2016-08-04 07:13:53.802636

"""

# revision identifiers, used by Alembic.
revision = 'a46a17bfd29b'
down_revision = 'a31c98c74ea0'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('batches_versions',
                    sa.Column('version_id', sa.Integer(), nullable=True),
                    sa.Column('batch_token', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['batch_token'], ['batch.token'], ),
                    sa.ForeignKeyConstraint(['version_id'], ['versions.id'], ))
    op.drop_column('batch', 'epvs')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('batch', sa.Column('epvs', postgresql.JSONB(), autoincrement=False,
                  nullable=True))
    op.drop_table('batches_versions')
    # ### end Alembic commands ###
