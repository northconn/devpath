# Unidade 11 — Desafio final e revisão

## Resultado esperado

Você entregará uma melhoria pequena, segura e reproduzível do Vet Environment Lab, com testes, qualidade, diagnóstico, histórico Git e retrospectiva verificáveis.

## Tempo estimado

240–360 minutos.

## Pré-requisitos

Unidades 0–10 concluídas, conta GitHub com MFA, Docker Compose, uv, Node/npm e uma cópia pessoal do repositório. Leia `docs/tooling-versions.md` antes de instalar versões.

## Por que isso importa

Uma entrega profissional combina código, evidência de que funciona, comunicação e recuperação diante de falhas. O resultado não é só uma tela ou comando; é algo que outra pessoa consegue preparar, revisar e reproduzir.

## Modelo mental

Requisito descreve necessidade; critério de aceitação descreve evidência observável de que ela foi atendida. A branch permite isolar a mudança; commits contam decisões em partes; PR transforma a mudança em conversa revisável; CI repete verificações em ambiente limpo. A retrospectiva registra decisão, dificuldade, evidência e próximo experimento, sem transformar falha em vergonha.

Este desafio parte de `starter/`: ele deliberadamente só executa `hello`, possui `pyproject.toml`, `uv.lock` e `infra/compose.yaml`. Você construirá módulos pequenos, seguindo a referência apenas para comparar decisões depois de tentar. A referência não deve ser copiada inteira: cada requisito abaixo define comportamento e evidência suficientes para criar sua própria implementação.

## Vocabulário

| Português | Inglês | Definição |
| --- | --- | --- |
| critério de aceitação | acceptance criterion | evidência verificável de requisito atendido |
| critério de avaliação | rubric | descrição de competências observáveis |
| integração contínua | CI | verificações repetidas em mudança publicada |
| regressão | regression | comportamento correto que volta a falhar |
| retrospectiva | retrospective | revisão breve de processo e aprendizado |
| fonte de verdade | source of truth | armazenamento autoritativo do dado |

## Demonstração guiada

1. Faça fork e clone do repositório. Na raiz, execute `git status`, leia o README, `projects/vet-environment-lab/starter/README.md` e `docs/tooling-versions.md`. Crie branch: `git switch -c feat/patient-summary-command`.
2. Prepare o ponto inicial: em `projects/vet-environment-lab/starter/python`, execute `uv sync` e `uv run vet-environment-lab hello`. Em `../infra`, copie `.env.example` para `.env`, execute `docker compose --env-file .env up -d`, depois `docker compose --env-file .env ps`; no starter, confirme que ambos estão `running`, pois esse Compose ainda não declara health checks. Para observar `healthy`, compare `solution/infra/compose.yaml` depois de subir a solução. Não publique `.env`.
3. Implemente, em etapas pequenas, um comando `summary` que receba `--name`, `--species` e `--birth-year`; aceite somente `bird`, `cat`, `dog`, `rabbit`, remova espaços, normalize espécie em minúsculas e rejeite nome vazio e ano futuro. Use funções pequenas em `src/vet_environment_lab/`, imports explícitos e um ponto de entrada CLI. Escreva testes unitários antes ou junto da regra. A forma JSON pode ser `{ "name": "Luna", "species": "dog", "birth_year": 2021 }`.
4. Mantenha dados sintéticos. Se adicionar persistência, use SQL com parâmetros separados da consulta e trate PostgreSQL como fonte de verdade; Redis pode guardar somente resumo com TTL. O requisito mínimo deste desafio é subir os dois serviços e executar o diagnóstico preparado, não copiar a integração completa da referência.
5. Produza uma falha preparada e segura: com ambos os serviços `running`, rode `docker compose --env-file .env stop redis` e compare `docker compose --env-file .env ps`; PostgreSQL continua `running` enquanto Redis fica parado. Restaure com `docker compose --env-file .env start redis`, confirme os dois como `running` e registre comando/saída. Para um health check da aplicação, compare o comando `uv run vet-environment-lab health` na solução depois que `solution/infra` estiver `healthy`. Não rode `down --volumes`.
6. Adicione as ferramentas de desenvolvimento no starter com `uv add --dev pytest ruff`, escreva testes e execute `uv run pytest`, `uv run ruff check .` e `uv run ruff format --check .` dentro de `starter/python`. Atualize o workflow raiz `.github/workflows/ci.yml` para que o job Python também sincronize esse diretório e execute esses três comandos; a CI deve testar sua implementação no starter, não apenas a referência. Para comparação TypeScript, em `solution/typescript`, rode `npm ci`, `npm run test`, `npm run lint`, `npm run format` e `npm run typecheck` sem misturar sua mudança Python nessa referência.
7. Revise `git diff`, selecione arquivos com `git add caminho`, revise `git diff --staged` e crie commits compreensíveis, por exemplo `feat: add patient summary command` e `test: cover invalid patient summary`. Envie a branch. Abra issue e PR preenchendo `.github/pull_request_template.md`, incluindo objetivo, critérios, testes, diagnóstico, riscos e retrospectiva. Anexe somente saídas sem segredos.
8. Aguarde todos os jobs obrigatórios da CI ficarem verdes antes de solicitar revisão. Se algum falhar, escolha job e step, rode localmente o comando exibido e acrescente ao PR causa, correção e nova evidência verde.

## Exercício prático

**Objetivo:** entregar o comando `summary` e sua evidência de qualidade. **Ponto de partida:** `starter/python` e `starter/infra`; não copie o diretório `solution/`. **Segurança:** use somente dados fictícios, ignore `.env`, mantenha portas em `127.0.0.1`, não concatene entrada em SQL e não force push. **Aceitação:** `summary` válido imprime os três campos normalizados; entradas inválidas têm mensagem útil e saída diferente de zero; existem testes de sucesso e falha; serviços do starter sobem como `running`; Redis parado é diagnosticado e restaurado; a CI executa os testes/checks do starter e fica verde; commits são pequenos e PR usa o template. **Verificação:** guarde as saídas de `hello`, `summary`, testes, qualidade, `docker compose ps`, `git log --oneline`, link do PR e URL da execução verde da CI. **Pistas graduais:** (1) comece por uma função de validação sem Docker; (2) use `argparse` para argumentos; (3) compare arquivos da solução por responsabilidade, não por cópia. Consulte o [spoiler comentado](../solutions/11-final-challenge-solution.md) somente após sua entrega.

## Desafio

Escolha uma melhoria adicional sem ampliar escopo clínico: permitir `--species` com espaços e caixa mista, ou incluir uma função de resumo que devolva cópia de dados validados. Escreva primeiro um teste vermelho, faça a mudança mínima e explique no PR por que não foi necessário banco para testar a regra.

## Se algo deu errado

| Sintoma | Causa provável | Verificação |
| --- | --- | --- |
| `hello` funciona, `summary` não existe | ponto de entrada não encaminha subcomando | `uv run vet-environment-lab --help`, depois leia `__main__.py` |
| serviços não ficam `running` | `.env` ausente, porta ocupada ou Docker parado | `docker compose --env-file .env ps` e logs do serviço específico |
| PostgreSQL `running`, Redis parado | cache indisponível isoladamente | pare/inicie apenas Redis e registre ambos os estados |
| teste passa localmente, CI falha | ambiente ou comando da CI diferente | compare step, versões e lockfile |
| PR contém `.env` | staging selecionou arquivo sensível | remova do staging antes de publicar e reveja `git diff --staged` |

## Checkpoint

- [ ] Reproduzo o ambiente a partir de README, lockfile e Compose.
- [ ] Entreguei regra validada com testes e verificações locais.
- [ ] Registrei e recuperei uma falha preparada sem apagar dados.
- [ ] Tenho branch, commits, issue/PR com template, CI verde, evidências e retrospectiva.

## Perguntas de reflexão

1. Que evidências demonstram que outra pessoa consegue reproduzir seu ambiente?
2. Como você explicaria por que a parada do Redis não deve apagar o PostgreSQL?
3. Qual decisão sua foi menor que copiar a referência e por que ela reduz risco?

## Aprofundamento

Pesquise **“acceptance criteria observable software delivery”**, **“GitHub pull request review checklist”** e **“Docker Compose healthcheck status”**. Leia [GitHub: pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests) (essencial), [Docker Compose](https://docs.docker.com/compose/) (essencial) e [uv em GitHub Actions](https://docs.astral.sh/uv/guides/integration/github/) (complementar).

## Resumo

- Uma entrega é código, testes, diagnóstico e comunicação reproduzível.
- Critérios observáveis tornam revisão justa e objetiva.
- Starter é ponto de construção; referência serve para comparação posterior.
- Branch, commits, PR e CI deixam a evolução auditável.

## Rubrica de avaliação

| Competência | Evidência observável | A desenvolver | Atende | Supera |
| --- | --- | --- | --- | --- |
| Ambiente e reprodução | comandos, lockfile e estado Compose registrados | só relato verbal | outro aluno repete os passos | explica versões e uma diferença local/CI |
| Implementação e segurança | `summary`, dados sintéticos, validação e nenhum segredo | comando incompleto ou dado sensível | critérios funcionais atendidos | separa regra/CLI e justifica SQL/cache se usados |
| Testes e qualidade | teste vermelho, verde e checks executados | só execução manual | sucesso e falha cobertos; checks verdes | explica qual classe de defeito cada check cobre |
| Diagnóstico | falha Redis preparada, evidência e recuperação | diagnóstico por tentativa aleatória | hipótese, comando, saída e restauração | diferencia serviço, porta, credencial e aplicação |
| Git e colaboração | branch, commits, issue, PR e revisão de diff | commit amplo sem contexto | histórico legível e PR preenchido | responde a feedback com evidência e CI verde |
| Retrospectiva | decisões, dificuldade, evidência e próximo estudo | lista vaga | relata uma decisão e uma investigação | identifica melhoria concreta de processo |
