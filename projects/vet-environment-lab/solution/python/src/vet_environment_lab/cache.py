"""Cache Redis de resumos; nunca é a fonte de verdade."""

import json

import redis

from .config import Settings
from .models import Patient


def connect(settings: Settings) -> redis.Redis:
    return redis.Redis(
        host=settings.redis_host,
        port=settings.redis_port,
        decode_responses=True,
        socket_connect_timeout=3,
    )


def cache_key(name: str) -> str:
    return f"patient-summary:{name.lower()}"


def save_summary(settings: Settings, patient: Patient) -> None:
    client = connect(settings)
    try:
        client.setex(
            cache_key(patient.name),
            settings.summary_ttl_seconds,
            json.dumps(patient.summary()),
        )
    finally:
        client.close()


def get_summary(settings: Settings, name: str) -> Patient | None:
    client = connect(settings)
    try:
        raw_summary = client.get(cache_key(name))
    finally:
        client.close()
    return Patient(**json.loads(raw_summary)) if raw_summary else None


def check_redis(settings: Settings) -> None:
    client = connect(settings)
    try:
        client.ping()
    finally:
        client.close()
