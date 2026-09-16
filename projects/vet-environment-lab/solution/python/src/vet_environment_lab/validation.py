"""Regras de entrada fáceis de testar e explicar."""

from datetime import date

from .models import PatientInput

ALLOWED_SPECIES = frozenset({"bird", "cat", "dog", "rabbit"})


class ValidationError(ValueError):
    """Indica uma entrada que não atende às regras do laboratório."""


def validate_patient(name: str, species: str, birth_year: int) -> PatientInput:
    """Normaliza e valida dados sintéticos de nome, espécie e ano."""
    normalized_name = name.strip()
    normalized_species = species.strip().lower()
    current_year = date.today().year
    if not 2 <= len(normalized_name) <= 80:
        raise ValidationError("name must contain between 2 and 80 characters")
    if normalized_species not in ALLOWED_SPECIES:
        choices = ", ".join(sorted(ALLOWED_SPECIES))
        raise ValidationError(f"species must be one of: {choices}")
    if not 1900 <= birth_year <= current_year:
        raise ValidationError(f"birth_year must be between 1900 and {current_year}")
    return PatientInput(normalized_name, normalized_species, birth_year)
