from datetime import date

import pytest

from vet_environment_lab.validation import ValidationError, validate_patient


def test_validate_patient_normalizes_valid_synthetic_input() -> None:
    patient = validate_patient("  Luna  ", "DOG", 2021)
    assert patient.name == "Luna"
    assert patient.species == "dog"
    assert patient.birth_year == 2021


@pytest.mark.parametrize(
    ("name", "species", "birth_year", "message"),
    [
        (" ", "dog", 2021, "name"),
        ("Luna", "iguana", 2021, "species"),
        ("Luna", "dog", date.today().year + 1, "birth_year"),
    ],
)
def test_validate_patient_rejects_invalid_input(
    name: str, species: str, birth_year: int, message: str
) -> None:
    with pytest.raises(ValidationError, match=message):
        validate_patient(name, species, birth_year)
