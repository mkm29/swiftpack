"""init

Revision ID: 842abcd80d3e
Revises:
Create Date: 2023-07-10 17:10:45.380832

"""

from alembic import op
import sqlalchemy as sa
import sqlmodel  # NEW


# revision identifiers, used by Alembic.
revision = "842abcd80d3e"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "song",
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("artist", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("song")
    # ### end Alembic commands ###
