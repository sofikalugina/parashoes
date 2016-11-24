"""Added type and is_active columns for Attribute model

Revision ID: 465198720c97
Revises: ae7d3fc15970
Create Date: 2016-11-16 23:04:49.791927

"""

# revision identifiers, used by Alembic.
revision = '465198720c97'
down_revision = 'ae7d3fc15970'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('attribute', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.add_column('attribute', sa.Column('type', sa.String(), nullable=False, server_default='int'))
    op.alter_column('product', 'slug_name',
               existing_type=sa.TEXT(),
               nullable=True)
    op.create_index('idx_product_attribute_values_id', 'product_attribute_values', ['product_id', 'attribute_value_id'], unique=False)
    op.create_index('idx_product_type_attribute_value_id', 'product_type_attribute_value', ['product_type_id', 'attribute_value_id'], unique=False)
    op.alter_column('user', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'created_at',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.drop_index('idx_product_type_attribute_value_id', table_name='product_type_attribute_value')
    op.drop_index('idx_product_attribute_values_id', table_name='product_attribute_values')
    op.alter_column('product', 'slug_name',
               existing_type=sa.TEXT(),
               nullable=False)
    op.drop_column('attribute', 'type')
    op.drop_column('attribute', 'is_active')
    ### end Alembic commands ###