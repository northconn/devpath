# Ponto de partida

Execute o primeiro resultado em `python/`:

```bash
uv run vet-environment-lab hello
```

## Tarefas incrementais

1. Leia `src/vet_environment_lab/__main__.py` e execute `hello`. Antes, preveja quais dados seguros serão mostrados.
2. Crie uma função de validação para `name`, `species` e `birth_year`. Use dados fictícios; recuse nome vazio, espécie fora da lista e ano futuro.
3. Escreva testes para uma entrada válida e uma inválida.
4. Em `infra/`, copie `.env.example` para `.env`, suba PostgreSQL e Redis e confirme o estado com `docker compose ps`.
5. Na solução, localize a consulta SQL. Explique por que os valores aparecem como parâmetros, e não concatenados na string SQL.

## Se algo deu errado

- `uv: command not found`: instale o uv e abra um novo terminal; confirme com `uv --version`.
- A porta já está em uso: escolha outra porta no `.env` local e execute o Compose novamente.
- Serviço `unhealthy`: execute `docker compose logs postgres` ou `docker compose logs redis`; confira se o `.env` existe e se os nomes das variáveis coincidem.

## Uso no trabalho

Um projeto real costuma fornecer um ponto inicial, uma configuração de serviços e verificações. A habilidade útil não é decorar os comandos: é ler a saída, formar uma hipótese e guardar evidências reproduzíveis.

> Spoiler: a solução de referência fica em `../../solution/`.
