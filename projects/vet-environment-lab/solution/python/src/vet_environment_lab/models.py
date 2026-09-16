"""Tipos simples para um paciente estritamente fictício."""

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class PatientInput:
    name: str
    species: str
    birth_year: int


@dataclass(frozen=True)
class Patient(PatientInput):
    id: int

    def summary(self) -> dict[str, int | str]:
        return asdict(self)
