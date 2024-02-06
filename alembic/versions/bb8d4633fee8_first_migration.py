"""First Migration

Revision ID: bb8d4633fee8
Revises: 
Create Date: 2024-02-06 22:58:07.716398

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey

# revision identifiers, used by Alembic.
revision: str = 'bb8d4633fee8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'person',
        Column('PersonID', Integer, primary_key=True, autoincrement=True),
        Column('Name', String(50), nullable=False),
        Column('DoB', Date, nullable=False),
        Column('CountryOfResidency', String(50), nullable=False),
        Column('Nationality', String(25), nullable=False),
        Column('Occupation', String(25), nullable=False),
        Column('PEPStatus', Boolean),
        Column('SourceOfWealth', String(25))
    )

    op.create_table(
        'company',
        Column('CompanyID', Integer, primary_key=True, autoincrement=True),
        Column('Name', String(50), nullable=False),
        Column('Industry', String(25), nullable=False),
        Column('CountryofHeadquarters', String(50), nullable=False),
        Column('Type', String(25), nullable=False),
    )

    op.create_table(
        'person_company',
        Column('PersonID', Integer, ForeignKey('person.PersonID'), primary_key=True),
        Column('CompanyID', Integer, ForeignKey('company.CompanyID'), primary_key=True),
        Column('Role', String(25), nullable=False),
    )

def downgrade() -> None:
    pass
