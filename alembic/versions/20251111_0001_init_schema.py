"""init schema

Revision ID: 20251111_0001
Revises: 
Create Date: 2025-11-11 00:01:00
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "20251111_0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "clients",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("nom", sa.String(length=50), nullable=False),
        sa.Column("prenom", sa.String(length=50), nullable=False),
        sa.Column("mail", sa.String(length=100), nullable=False, unique=True),
        sa.Column("adresse", sa.String(length=255), nullable=True),
        sa.Column("numero", sa.String(length=20), nullable=True),
    )
    op.create_index("ix_clients_id", "clients", ["id"])
    op.create_index("uq_clients_mail", "clients", ["mail"], unique=True)

    op.create_table(
        "reservations",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("id_client", sa.Integer(), nullable=True),
        sa.Column("nom_reservation", sa.String(length=100), nullable=False),
        sa.Column("date_debut", sa.Date(), nullable=False),
        sa.Column("date_fin", sa.Date(), nullable=False),
        sa.Column("prix", sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(["id_client"], ["clients.id"]),
    )
    op.create_index("ix_reservations_id", "reservations", ["id"])
    op.create_index("ix_reservations_client_dates", "reservations", ["id_client", "date_debut", "date_fin"])


def downgrade() -> None:
    op.drop_index("ix_reservations_client_dates", table_name="reservations")
    op.drop_index("ix_reservations_id", table_name="reservations")
    op.drop_table("reservations")
    op.drop_index("uq_clients_mail", table_name="clients")
    op.drop_index("ix_clients_id", table_name="clients")
    op.drop_table("clients")


