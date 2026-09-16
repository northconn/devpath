# Spoiler — Unidade 10

## Resposta trabalhada

Um teste para o defeito de normalização pode usar os dados fictícios abaixo:

```python
def test_validate_patient_normalizes_mixed_case_species() -> None:
    patient = validate_patient(" Mimo ", " CAT ", 2020)
    assert patient.species == "cat"
```

Ao remover temporariamente `.lower()`, o teste deve falhar porque `CAT` não está em `ALLOWED_SPECIES`. Restaurar `.lower()` é a mudança mínima que devolve verde. Em seguida rode:

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

Na falha TypeScript, `birth_year: '2021'` é texto, mas `PatientInput` pede `number`; corrija para `birth_year: 2021`. Não use `any`: isso remove a evidência que a checagem ofereceu. Um teste Python verde não executa a ferramenta TypeScript, então não contradiz esse erro de CI.
