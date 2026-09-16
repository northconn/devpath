"""Interface de linha de comando do laboratório."""

import argparse
import json
import platform
import sys

import psycopg
import redis

from . import cache, database
from .config import Settings
from .models import Patient
from .validation import ValidationError, validate_patient


def hello() -> None:
    print("Olá, Vet Environment Lab!")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Sistema: {platform.system()} {platform.release()}")
    print("Os exemplos usam somente dados fictícios.")


def health(settings: Settings) -> bool:
    checks: dict[str, str] = {}
    for service, check in (
        ("postgres", database.check_postgres),
        ("redis", cache.check_redis),
    ):
        try:
            check(settings)
            checks[service] = "healthy"
        except Exception as error:
            checks[service] = f"unhealthy: {type(error).__name__}: {error}"
    print(json.dumps(checks, ensure_ascii=False, indent=2))
    if "unhealthy" in " ".join(checks.values()):
        print(
            "Dica: em ../infra, copie .env.example para .env e execute "
            "docker compose --env-file .env up -d."
        )
        return False
    return True


def print_patient(patient: Patient, source: str) -> None:
    print(
        json.dumps({"source": source, "patient": patient.summary()}, ensure_ascii=False)
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Cadastro de pacientes inteiramente fictícios"
    )
    subcommands = parser.add_subparsers(dest="command", required=True)
    subcommands.add_parser("hello", help="mostra informações seguras do ambiente")
    subcommands.add_parser("health", help="diagnostica PostgreSQL e Redis")
    for command in ("validate", "add"):
        item = subcommands.add_parser(command)
        item.add_argument("--name", required=True)
        item.add_argument("--species", required=True)
        item.add_argument("--birth-year", required=True, type=int)
    get_command = subcommands.add_parser(
        "get", help="busca primeiro o resumo temporário"
    )
    get_command.add_argument("--name", required=True)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    settings = Settings()
    try:
        if args.command == "hello":
            hello()
        elif args.command == "health":
            if not health(settings):
                raise SystemExit(1)
        elif args.command == "validate":
            patient = validate_patient(args.name, args.species, args.birth_year)
            print(json.dumps(patient.__dict__, ensure_ascii=False))
        elif args.command == "add":
            patient = validate_patient(args.name, args.species, args.birth_year)
            saved_patient = database.save_patient(settings, patient)
            cache.save_summary(settings, saved_patient)
            print_patient(saved_patient, "postgres and redis")
        elif args.command == "get":
            cached_patient = cache.get_summary(settings, args.name)
            if cached_patient is not None:
                print_patient(cached_patient, "redis cache")
                return
            patient = database.find_patient_by_name(settings, args.name)
            if patient is None:
                print("Patient was not found in PostgreSQL.")
                raise SystemExit(2)
            cache.save_summary(settings, patient)
            print_patient(patient, "postgres; redis cache refreshed")
    except ValidationError as error:
        print(f"Invalid fictional patient: {error}", file=sys.stderr)
        raise SystemExit(2) from error
    except (OSError, redis.RedisError, psycopg.Error) as error:
        print(
            f"Service operation failed: {type(error).__name__}: {error}",
            file=sys.stderr,
        )
        print(
            "Run the health command for a PostgreSQL and Redis diagnosis.",
            file=sys.stderr,
        )
        raise SystemExit(1) from error
