# Gabarito comentado — Checkpoints das Unidades 6–11

1. **B.** `.venv` criado por `uv sync` contém a instalação baseada no lockfile. Tema e extensões não escolhem runtime; abrir sem pasta não configura o projeto.
2. Use `lower()`, pois `str` não possui `lowercase()`. A stack trace aponta arquivo e linha da chamada; leia a última linha para o tipo/erro e suba até a primeira linha que pertence ao seu código.
3. **C.** Staging seleciona o conteúdo do próximo retrato. `git add` não envia nada; `git commit` é local; PR reúne commits para revisão.
4. Leia a intenção de ambas as branches e escolha, por exemplo, `cache_ttl_seconds=120 # temporary cache` se o novo TTL é decisão funcional e o comentário segue útil. Edite removendo marcadores, rode `git add settings.txt`, faça commit de resolução e teste/revise o resultado. Não use força ou reescrita de histórico.
5. **C.** `pyproject.toml` declara intenção; `uv.lock` guarda a resolução para instalação repetível. README explica uso, e `__init__.py` organiza pacote.
6. Os testes ainda comprovam os comportamentos que cobrem; eles não comprovam estilo. Abra o arquivo indicado, aplique `uv run ruff format .`, revise o diff e rode novamente o check. Não desative formatter para obter verde.
7. **C.** Tipos TypeScript são verificados no desenvolvimento e não validam por si valores que chegam em execução. `validatePatient` protege a fronteira real; ESM organiza módulos.
8. Colete: log completo do job e step, comando exato e versão Node/TypeScript usadas pelo runner, e diff de `package.json`/`package-lock.json` e arquivo apontado. Depois reproduza localmente com `npm ci` e o comando do log.
9. **C.** Redis é cache temporário; PostgreSQL é fonte persistente. Apagar volume destrói evidência, e expor porta viola o escopo local.
10. Inclua objetivo e critérios, branch/commits, comandos e saídas sem segredos para `hello`, `summary`, testes/qualidade e `docker compose ps`, diagnóstico e recuperação do Redis, versões/lockfiles relevantes, link da issue/PR e resultado de CI se houver. `.env`, tokens e dados pessoais ficam fora.
