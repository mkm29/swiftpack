"""initial schema

Revision ID: 2be243c97790
Revises:
Create Date: 2024-06-19 18:04:44.381364

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2be243c97790"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "genre",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "artist",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("genre_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["genre_id"],
            ["genre.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "show",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("venue", sa.String(), nullable=True),
        sa.Column("date", sa.String(), nullable=True),
        sa.Column("time", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "artist_show",
        sa.Column("artist_id", sa.Integer(), nullable=True),
        sa.Column("show_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["artist_id"],
            ["artist.id"],
        ),
        sa.ForeignKeyConstraint(
            ["show_id"],
            ["show.id"],
        ),
    )
    op.create_table(
        "genre_artist",
        sa.Column("genre_id", sa.Integer(), nullable=True),
        sa.Column("artist_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["artist_id"],
            ["artist.id"],
        ),
        sa.ForeignKeyConstraint(
            ["genre_id"],
            ["genre.id"],
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("genre_artist")
    op.drop_table("artist_show")
    op.drop_table("show")
    op.drop_table("artist")
    op.drop_table("genre")
    # ### end Alembic commands ###
