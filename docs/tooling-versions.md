# Versões e compatibilidade

Verificado em 16 de setembro de 2026. Antes de estudar, use `--version`; o número instalado é mais útil que memorizar este documento.

| Ferramenta | Faixa adotada | Motivo e referência |
| --- | --- | --- |
| Python | >= 3.12, versão estável | [Python](https://www.python.org/downloads/) e [uv sync](https://docs.astral.sh/uv/concepts/projects/sync/) — o projeto exige 3.12 ou superior |
| uv | >= 0.6, versão estável | [instalação oficial](https://docs.astral.sh/uv/getting-started/installation/) — gerencia Python, ambiente, dependências e lockfile |
| Node.js | >= 24 e linha 24 LTS | [ciclos de lançamento](https://nodejs.org/en/about/previous-releases) — LTS reduz mudanças inesperadas |
| npm | >= 11, fornecido pelo Node 24 | [npm ci](https://docs.npmjs.com/cli/commands/npm-ci/) — respeita lockfile |
| Docker Engine/Desktop | versão estável com Compose v2 | [Compose](https://docs.docker.com/compose/) — `docker compose`, não o binário legado |
| PostgreSQL | imagem `postgres:17-alpine` | [imagem oficial](https://hub.docker.com/_/postgres) — declarada em `compose.yaml` |
| Redis | imagem `redis:7-alpine` | [imagem oficial](https://hub.docker.com/_/redis) — declarada em `compose.yaml` |

Python e dependências estão fixados em `uv.lock`; TypeScript e ferramentas em `package-lock.json`. Não atualize lockfiles por hábito: leia o diff, rode as verificações e registre o motivo.

## GitHub Actions

O workflow [CI](../.github/workflows/ci.yml) foi conferido em 16 de setembro de 2026 contra os repositórios oficiais. As ações abaixo usam o commit da tag indicada; o SHA evita que uma alteração futura da tag modifique uma execução já revisada.

| Ação | Tag conferida | SHA fixado |
| --- | --- | --- |
| [actions/checkout](https://github.com/actions/checkout) | `v7` | `3d3c42e5aac5ba805825da76410c181273ba90b1` |
| [actions/setup-node](https://github.com/actions/setup-node) | `v7` | `820762786026740c76f36085b0efc47a31fe5020` |
| [astral-sh/setup-uv](https://github.com/astral-sh/setup-uv) | `v10.1.0` | `bec219d24cd3e171d82865faccec33120bb574f4` |

Na referência, a CI sincroniza o lockfile e executa pytest, Ruff e TypeScript. No starter, ela confirma o `hello` enquanto o ponto de partida ainda não contém testes nem Ruff. Quando você cumprir a Unidade 11 e adicionar essas ferramentas e testes ao starter, atualize o comando correspondente no workflow para executar as três verificações também nesse diretório.
