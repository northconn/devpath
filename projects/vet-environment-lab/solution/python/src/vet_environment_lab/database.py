"""Acesso explícito e parametrizado ao PostgreSQL."""

import psycopg
from psycopg.rows import dict_row

from .config import Settings
from .models import Patient, PatientInput

CREATE_PATIENTS_TABLE = """
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    species TEXT NOT NULL,
    birth_year INTEGER NOT NULL
)
"""


def connect(settings: Settings) -> psycopg.Connection:
    return psycopg.connect(
        host=settings.postgres_host,
        port=settings.postgres_port,
        dbname=settings.postgres_database,
        user=settings.postgres_user,
        password=settings.postgres_password,
        connect_timeout=3,
        row_factory=dict_row,
    )


def save_patient(settings: Settings, patient: PatientInput) -> Patient:
    """Grava no PostgreSQL, a fonte de verdade deste laboratório."""
    sql = """
    INSERT INTO patients (name, species, birth_year) VALUES (%s, %s, %s)
    ON CONFLICT (name) DO UPDATE
    SET species = EXCLUDED.species, birth_year = EXCLUDED.birth_year
    RETURNING id, name, species, birth_year
    """
    with connect(settings) as connection:
        connection.execute(CREATE_PATIENTS_TABLE)
        row = connection.execute(
            sql, (patient.name, patient.species, patient.birth_year)
        ).fetchone()
    if row is None:
        raise RuntimeError("PostgreSQL did not return the saved patient")
    return Patient(**row)


def find_patient_by_name(settings: Settings, name: str) -> Patient | None:
    """Busca o registro persistente com uma consulta parametrizada."""
    sql = "SELECT id, name, species, birth_year FROM patients WHERE name = %s"
    with connect(settings) as connection:
        connection.execute(CREATE_PATIENTS_TABLE)
        row = connection.execute(sql, (name,)).fetchone()
    return Patient(**row) if row else None


def check_postgres(settings: Settings) -> None:
    with connect(settings) as connection:
        connection.execute("SELECT 1")
