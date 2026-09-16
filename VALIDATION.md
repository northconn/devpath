# Validação

Executado em 16 de setembro de 2026, em Linux sob WSL2. Os comandos abaixo foram executados na cópia de trabalho; dados usados no laboratório são sintéticos.

## Material e automação

| Verificação | Comando | Resultado |
| --- | --- | --- |
| Links Markdown e navegação local | `python3 scripts/check_markdown_links.py` | Passou: `Links Markdown locais: OK`. O script percorre os arquivos Markdown do repositório, ignora `.git`, `.venv` e `node_modules`, e verifica destinos locais e âncoras. |
| Sintaxe do verificador | `python3 -m py_compile scripts/check_markdown_links.py` | Passou. |
| Espaços e conflitos de diff | `git diff --check` | Passou. |
| YAML da CI | Em `solution/typescript`, `PATH=/home/vflopes/.nvm/versions/node/v24.19.0/bin:$PATH ./node_modules/.bin/prettier --check ../../../../.github/workflows/ci.yml` | Passou: o Prettier analisou o YAML sem alterações necessárias. A execução remota do GitHub Actions depende de push ou PR. |
| Ações usadas pela CI | `git ls-remote` nos repositórios oficiais das ações | Tags conferidas: checkout `v7`, setup-node `v7` e setup-uv `v10.1.0`; SHAs documentados em `docs/tooling-versions.md`. |
| Busca de padrões de segredo | `rg -n --hidden -g '!.git/**' -g '!**/.venv/**' -g '!**/node_modules/**' -e 'AKIA[0-9A-Z]{16}' -e 'gh[pousr]_[A-Za-z0-9]{20,}' -e 'sk-[A-Za-z0-9]{20,}' -e 'xox[baprs]-[A-Za-z0-9-]{20,}' .` | Sem saída; `rg` retornou código 1, esperado quando não encontra correspondências. |

## Projetos

| Verificação | Comando | Resultado |
| --- | --- | --- |
| Starter Python | `uv sync --locked` e `uv run vet-environment-lab hello` em `starter/python` | Passou. O starter mostrou o primeiro resultado e não possui pytest, Ruff nem testes ainda. |
| Referência Python | `uv sync --locked`, `uv run pytest`, `uv run ruff check .` e `uv run ruff format --check .` em `solution/python` | Passou: 4 testes, Ruff sem problemas e 9 arquivos já formatados. |
| Referência TypeScript | `PATH=/home/vflopes/.nvm/versions/node/v24.19.0/bin:$PATH npm ci`, `npm run test`, `npm run lint`, `npm run format` e `npm run typecheck` | Passou com Node `v24.19.0` e npm `12.0.2`: 6 testes, lint, formatação e tipos sem falhas. |

## Serviços locais

O Compose da solução só referencia imagens oficiais `postgres:17-alpine` e `redis:7-alpine`; não existe Dockerfile nem imagem própria a construir.

| Verificação | Comando | Resultado |
| --- | --- | --- |
| Configuração | `docker compose -f ../infra/compose.yaml config -q` com `POSTGRES_PORT=15432` e `REDIS_PORT=16379` | Passou. |
| Imagens e serviços | `docker compose -f ../infra/compose.yaml pull` e `up -d --wait --wait-timeout 60` | Passou; PostgreSQL e Redis ficaram `healthy` em `127.0.0.1:15432` e `127.0.0.1:16379`. |
| Diagnóstico | `uv run vet-environment-lab health` com as mesmas variáveis | Passou: PostgreSQL e Redis responderam `healthy`. |
| Fluxo sintético | `uv run vet-environment-lab add --name T05-Validation --species ' DOG ' --birth-year 2021`, seguido de `get --name T05-Validation` | Passou: espécie normalizada para `dog`; leitura retornou `redis cache`. |
| Encerramento seguro | `docker compose -f ../infra/compose.yaml down` | Executado sem `--volumes`; volumes nomeados foram preservados. |

## Revisão de plataforma e limites

As instruções existentes para Ubuntu, Windows com WSL2 e macOS foram revisadas em `docs/setup-ubuntu.md`, `docs/setup-windows-wsl.md` e `docs/setup-macos.md`. A validação prática ocorreu apenas em Linux/WSL2; Windows nativo e macOS não foram executados manualmente. A CI ainda precisa de uma execução real no GitHub após o próximo push ou PR.
