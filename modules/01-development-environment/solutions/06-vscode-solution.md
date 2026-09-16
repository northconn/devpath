# Spoiler — Unidade 6

## Resposta trabalhada

Com o breakpoint em `normalized_name = name.strip().lowercase()`, o valor de `name` é um espaço e `normalized_name` ainda não recebeu valor. Ao avançar, a stack trace termina naquela linha com `AttributeError`, pois `str` oferece `lower()`, não `lowercase()`. A correção deste bug preparado é restaurar a linha original `normalized_name = name.strip()`; a normalização de caixa pertence à espécie, na linha seguinte.

Depois de desfazer a alteração, executei:

```bash
cd projects/vet-environment-lab/solution/python
uv run vet-environment-lab validate --name "  LUNA  " --species DOG --birth-year 2021
```

O JSON normaliza a espécie para `dog` e remove espaços das extremidades do nome. O comando não exige Docker: `validate` chama `validate_patient`; `Settings()` apenas reúne valores de configuração. A nota de diagnóstico deve guardar configuração/argumentos, saída, arquivo/linha, valor observado, hipótese confirmada e restauração, nunca `.env`.
