"""Configuração local recebida do ambiente, sem imprimir senhas."""

from dataclasses import dataclass
from os import getenv


@dataclass(frozen=True)
class Settings:
    postgres_host: str = getenv("POSTGRES_HOST", "127.0.0.1")
    postgres_port: int = int(getenv("POSTGRES_PORT", "5432"))
    postgres_database: str = getenv("POSTGRES_DB", "vet_lab_dev")
    postgres_user: str = getenv("POSTGRES_USER", "vet_lab_app")
    postgres_password: str = getenv("POSTGRES_PASSWORD", "local_development_only")
    redis_host: str = getenv("REDIS_HOST", "127.0.0.1")
    redis_port: int = int(getenv("REDIS_PORT", "6379"))
    summary_ttl_seconds: int = 300
