# Spoiler — Unidade 5

## Resposta trabalhada

Com serviços saudáveis, no diretório `solution/python` executei:

```bash
uv run vet-environment-lab health
uv run vet-environment-lab add --name "Luna" --species dog --birth-year 2021
uv run vet-environment-lab get --name "Luna"
uv run vet-environment-lab get --name "Luna"
```

A segunda leitura deve indicar `redis cache`. No diretório `solution/infra`, `docker compose --env-file .env exec -T redis redis-cli TTL patient-summary:luna` deve retornar inteiro positivo e diminuir depois de alguns segundos. Quando a chave expira, uma leitura repõe o cache a partir de PostgreSQL; por isso expiração não perde o registro.

As instruções SQL usam `patient_demo` para não confundir a tabela do aplicativo. `CREATE`, `INSERT`, `SELECT`, `UPDATE` e `DELETE` deixam mensagens como `CREATE TABLE`, `INSERT 0 1`, uma linha selecionada, `UPDATE 1` e `DELETE 1`. Se só PostgreSQL falhar no health check, verifique serviço, porta, URL e nomes de `.env.example`; se só Redis falhar, o banco continua a fonte de verdade. No código, `%s` e a tupla de valores separam instrução SQL de entrada e continuam necessários mesmo com validação.
