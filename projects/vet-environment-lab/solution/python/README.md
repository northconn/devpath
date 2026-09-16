# Aplicação Python

Execute `uv sync --all-groups` para criar o ambiente isolado a partir de `pyproject.toml` e `uv.lock`. Use `uv run vet-environment-lab --help` para descobrir os comandos.

Os testes de validação não precisam de Docker. `add`, `get` e `health` usam os serviços de `../infra/`. A aplicação usa valores locais compatíveis com `.env.example`; exporte as variáveis de ambiente se trocar as portas.
