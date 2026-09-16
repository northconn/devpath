# Unidade 5 — Bancos de dados: PostgreSQL e Redis

## Resultado esperado

Você persistirá um paciente fictício no PostgreSQL, consultará um resumo com cache Redis e diagnosticará falhas de serviço, credencial, porta e consulta.

## Tempo estimado

120–170 minutos.

## Pré-requisitos

Unidade 4, serviços saudáveis e `uv` funcional.

## Por que isso importa

Uma variável em memória desaparece quando o processo encerra; dados importantes precisam de uma fonte persistente com regras. Um cache acelera leitura, mas não pode apagar a responsabilidade do banco principal.

## Modelo mental

Banco relacional organiza tabelas (coleções), linhas (registros), colunas (atributos), schema (estrutura) e tipos. Chave primária identifica uma linha; chave estrangeira liga tabelas. PostgreSQL preserva os registros e aplica restrições. SQL cria e consulta: `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`. Parâmetros enviam valores separados da consulta, prevenindo SQL injection; jamais forme SQL concatenando entrada. Uma transação agrupa ações: ACID resume atomicidade, consistência, isolamento e durabilidade. Índice acelera algumas buscas, mas custa espaço e escrita. Redis armazena chaves e valores, com listas, hashes e outros tipos; TTL expira valores. Aqui Redis só guarda resumo temporário: PostgreSQL é fonte de verdade.

## Vocabulário

| Português | Inglês | Definição |
| --- | --- | --- |
| tabela / linha / coluna | table / row / column | estrutura, registro e atributo |
| schema | schema | definição organizada de tabelas e regras |
| chave primária | primary key | identificador único da linha |
| consulta parametrizada | parameterized query | SQL e valores enviados separadamente |
| transação / ACID | transaction / ACID | conjunto confiável de alterações / suas propriedades |
| cache / TTL | cache / time to live | cópia temporária / prazo de validade |

## Demonstração guiada

1. A partir da raiz, execute `cd projects/vet-environment-lab/solution/infra`, `cp .env.example .env` se necessário, `docker compose --env-file .env up -d` e `docker compose --env-file .env ps`. Espere `healthy`.
2. Em outro terminal, execute `cd projects/vet-environment-lab/solution/python`, `uv sync --all-groups` e preveja o resultado de `uv run vet-environment-lab validate --name "Luna" --species dog --birth-year 2021`.
3. Execute o comando. Uma entrada inválida, como ano futuro, deve ser rejeitada antes do banco.
4. Execute `uv run vet-environment-lab health`. Ele informa separadamente conexão PostgreSQL e Redis, ajudando a isolar a causa.
5. Execute `uv run vet-environment-lab add --name "Luna" --species dog --birth-year 2021`, depois `uv run vet-environment-lab get --name "Luna"` duas vezes. A primeira pode preencher cache; a segunda deve mostrar `"source": "redis cache"` se houver TTL.
6. Para observar o TTL, no terminal `infra/` execute `docker compose --env-file .env exec -T redis redis-cli TTL patient-summary:luna`. O resultado é um número positivo em segundos; espere alguns segundos e rode de novo para vê-lo diminuir. `-1` significa chave sem expiração e `-2`, chave ausente.
7. Execute SQL explícito e sintético no terminal `infra/`; estas consultas usam uma tabela de demonstração independente do programa:

   ```bash
   docker compose --env-file .env exec -T postgres psql -U vet_lab_app -d vet_lab_dev -c 'CREATE TABLE IF NOT EXISTS patient_demo (id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY, name TEXT NOT NULL UNIQUE, species TEXT NOT NULL, birth_year INTEGER NOT NULL);'
   docker compose --env-file .env exec -T postgres psql -U vet_lab_app -d vet_lab_dev -c "INSERT INTO patient_demo (name, species, birth_year) VALUES ('Mimo', 'cat', 2020);"
   docker compose --env-file .env exec -T postgres psql -U vet_lab_app -d vet_lab_dev -c "SELECT id, name, species, birth_year FROM patient_demo WHERE name = 'Mimo';"
   docker compose --env-file .env exec -T postgres psql -U vet_lab_app -d vet_lab_dev -c "UPDATE patient_demo SET birth_year = 2019 WHERE name = 'Mimo';"
   docker compose --env-file .env exec -T postgres psql -U vet_lab_app -d vet_lab_dev -c "DELETE FROM patient_demo WHERE name = 'Mimo';"
   ```

   Os valores são fictícios. O `psql` é um cliente de administração local para aprender SQL; no código da aplicação, a entrada externa sempre deve ser parâmetro separado.
8. Abra `src/vet_environment_lab/database.py`. Encontre a consulta com parâmetros. Compare mentalmente com uma entrada contendo aspas: parâmetros preservam dado como valor, não como instrução SQL.

## Exercício prático

**Objetivo:** adicionar e recuperar dois pacientes sintéticos, distinguindo persistência de cache. **Ponto de partida:** serviços saudáveis em `projects/vet-environment-lab/solution/infra` e outro terminal em `solution/python`. **Segurança:** use somente nomes fictícios, não publique `.env`, mantenha SQL parametrizado e não exponha portas fora de `127.0.0.1`. **Aceitação:** dois `add` retornam êxito; `get` retorna cada resumo; `health` informa os dois serviços; e `TTL patient-summary:luna` é positivo após uma leitura. **Verificação:** pare apenas a aplicação (não o Compose) e execute `get` em novo comando; o PostgreSQL ainda é consultável. **Pistas graduais:** (1) `uv run vet-environment-lab --help` mostra os argumentos; (2) valide antes de adicionar; (3) cache expirar não significa perda do banco. Consulte o [spoiler comentado](../solutions/05-databases-solution.md) depois da sua tentativa.

## Desafio

No terminal `infra/`, pare somente Redis com `docker compose --env-file .env stop redis`. No terminal `python`, rode `uv run vet-environment-lab health` e anote a mensagem. De volta a `infra/`, execute `docker compose --env-file .env start redis`, espere, e no terminal `python` rode `uv run vet-environment-lab health`. Explique por que uma falha de cache não deve autorizar perda do PostgreSQL. Não remova containers ou volumes.

## Se algo deu errado

| Sintoma | Causa provável | Verificação |
| --- | --- | --- |
| health falha nos dois | Compose ou rede local não iniciou | `docker compose ps`, depois logs |
| PostgreSQL falha e Redis passa | credencial, porta ou banco isoladamente | compare `.env` local ao `.env.example`; leia logs postgres |
| Redis falha e PostgreSQL passa | cache parado ou URL errada | `docker compose ps redis`, logs e variável Redis |
| erro de consulta | schema, parâmetros ou dado inválido | leia a mensagem completa e teste `validate` primeiro |
| registro não aparece após reinício | volume ausente/removido | confira `compose.yaml` e histórico de comandos |

## Checkpoint

- [ ] Sei nomear tabela, linha, coluna, chave e schema.
- [ ] Executei `health`, `add` e `get` com dados sintéticos.
- [ ] Explico PostgreSQL como fonte de verdade e Redis como cache com TTL.

## Perguntas de reflexão

1. Que evidência distingue senha inválida de serviço indisponível?
2. O que se perde ao guardar o único registro de um paciente apenas no Redis?
3. Por que uma consulta parametrizada continua necessária quando a validação já rejeita entrada inválida?

## Aprofundamento

Pesquise **“PostgreSQL parameterized queries SQL injection”**, **“ACID transaction simple explanation”** e **“Redis EX TTL cache”**. Leia [tutorial PostgreSQL](https://www.postgresql.org/docs/current/tutorial.html) (essencial) e [Redis documentation](https://redis.io/docs/latest/) (essencial); procure exemplos de transação e expiração.

## Resumo

- Persistência exige regras e durabilidade além da memória do programa.
- SQL parametrizado separa instrução de dado e reduz injeção.
- Redis acelera cópias temporárias; PostgreSQL mantém o registro autoritativo.
