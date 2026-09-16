# Spoiler — Unidade 8

## Resposta trabalhada

Na referência, o limite está em `validation.py`:

```python
if not 1900 <= birth_year <= current_year:
    raise ValidationError(f"birth_year must be between 1900 and {current_year}")
```

O teste deve chamar a função com `1899` e verificar `ValidationError` com mensagem que inclua `birth_year`. Primeiro ele falha se a condição ainda aceita 1899; depois da condição mínima, ele passa junto com os casos existentes.

Para o desafio, uma implementação simples é `return sorted(ALLOWED_SPECIES)`. Ela cria uma lista nova; portanto `result.append("iguana")` não altera o `frozenset` exportado. Rode sempre `uv run pytest`, `uv run ruff check .` e `uv run ruff format --check .` no diretório do projeto.
