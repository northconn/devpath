# Spoiler — Unidade 4

## Resposta trabalhada

No diretório `projects/vet-environment-lab/solution/infra`, a sequência é:

```bash
cp .env.example .env
docker compose --env-file .env up -d
docker compose --env-file .env ps
docker compose --env-file .env logs postgres
docker compose --env-file .env logs redis
docker compose --env-file .env port postgres 5432
docker compose --env-file .env port redis 6379
docker compose --env-file .env down
```

`ps` deve mostrar `healthy`; `port` deve mostrar `127.0.0.1:5432` e `127.0.0.1:6379` para os valores padrão. Isso é prova do mapeamento, sem fingir que PostgreSQL fala HTTP. A falha segura é `POSTGRES_PORT=not-a-port docker compose --env-file .env config`: ela deve rejeitar a configuração antes de subir serviços. `unset POSTGRES_PORT` restaura o ambiente do shell. Imagem é a receita; container é uma execução. `down` preserva volume, enquanto `down --volumes` apagaria os dados persistentes.
