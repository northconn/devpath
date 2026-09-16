# Unidade 8 — Python moderno e organização em módulos

## Resultado esperado

Você executará o projeto Python com `uv`, explicará `pyproject.toml`, `uv.lock` e o layout `src/`, e adicionará uma regra pequena com teste antes de consultar a solução.

## Tempo estimado

150–210 minutos.

## Pré-requisitos

Unidades 0–7; Python 3.12 ou superior e `uv` disponíveis. Use `uv --version` e `uv run python --version` como evidência, não uma versão decorada.

## Por que isso importa

Uma equipe precisa que o programa rode de modo parecido na máquina local e na CI. Declarar dependências em `pyproject.toml` e resolver versões em `uv.lock` evita o caso de uma dependência instalada por acaso no computador de uma pessoa, mas ausente para outra.

## Modelo mental

Python é interpretado por um runtime que lê e executa módulos. `uv` gerencia a versão de Python, cria ambiente virtual isolado, sincroniza dependências e executa comandos no ambiente correto. `pyproject.toml` declara metadados, dependências e ferramentas; `uv.lock` registra a resolução concreta. Não edite lockfile manualmente nem o atualize sem revisar o diff.

Em `src/`, o pacote `vet_environment_lab` contém módulos (`validation.py`, `models.py`). `__init__.py` marca e organiza o pacote; `cli.py` traduz argumentos de terminal em chamadas; `validation.py` guarda regra de negócio. Separar entrada/saída de regra permite testar uma função sem abrir terminal, banco ou Redis. Importar um módulo lê seu nome; executar `python -m pacote` pede que Python execute o ponto de entrada do pacote.

## Vocabulário

| Português | Inglês | Definição |
| --- | --- | --- |
| interpretador | interpreter | runtime que executa Python |
| ambiente virtual | virtual environment | dependências isoladas por projeto |
| dependência | dependency | biblioteca da qual o projeto precisa |
| arquivo de bloqueio | lockfile | versões resolvidas para reprodução |
| módulo / pacote | module / package | arquivo Python / coleção importável de módulos |
| traceback | traceback | pilha e local de uma exceção |

## Demonstração guiada

1. Entre em `projects/vet-environment-lab/solution/python`. Leia `pyproject.toml`: `requires-python` estabelece o mínimo; `dependencies` são necessárias em execução; o grupo `dev` contém `pytest` e `ruff`. Compare com `uv.lock`, que é gerado e muito mais detalhado.
2. Execute, nesta ordem:

   ```bash
   uv sync --all-groups
   uv run python --version
   uv run vet-environment-lab hello
   uv run vet-environment-lab --help
   ```

   `sync` cria ou atualiza `.venv` a partir do lockfile. `uv run` garante que o comando usa aquele ambiente. A saída de `--help` é a fonte de argumentos aceitos pela CLI.
3. Abra `src/vet_environment_lab/models.py`, `validation.py` e `cli.py`. Siga os dados de `--name "  Luna  "`: `argparse` recebe texto, `validate_patient` remove espaços e normaliza espécie, e `PatientInput` contém os valores. Antes de executar, preveja a saída de `uv run vet-environment-lab validate --name "  Luna  " --species DOG --birth-year 2021`.
4. Execute o comando e depois uma entrada segura, mas inválida: `uv run vet-environment-lab validate --name "Luna" --species iguana --birth-year 2021`. A mensagem vem da exceção `ValidationError`; ela informa a regra e a CLI a transforma em saída compreensível com código 2.
5. Leia `tests/test_validation.py`. Cada caso usa Arrange–Act–Assert: prepara entrada, chama `validate_patient`, verifica resultado ou exceção. Rode `uv run pytest` e depois `uv run ruff check .` e `uv run ruff format --check .`.
6. Exercite variáveis e fluxo no console isolado, sem editar o projeto: `uv run python -c 'species = ["dog", "cat"]; print(", ".join(item.upper() for item in species))'`. Identifique a lista, o laço implícito e a função de saída. Para tratar erro simples, a aplicação usa `try`/`except` no `main`; não esconda exceções com `except Exception` sem registrar causa.
7. Quando uma dependência for necessária, declare a intenção com `uv add NOME`, leia as mudanças em `pyproject.toml` e `uv.lock`, rode testes e faça commit das duas. Nesta unidade não adicione dependência: as existentes bastam. Dependência instalada fora do ambiente isolado não é evidência de que o projeto a possui.

## Exercício prático

**Objetivo:** especificar e implementar uma regra para recusar ano de nascimento anterior a 1900. **Ponto de partida:** o código de referência já tem a regra; trabalhe primeiro em uma cópia própria ou no starter, criando `tests/test_validation.py` e os módulos mínimos necessários. **Segurança:** pacientes são inteiramente fictícios; não instale pacote fora de `uv` nem altere `uv.lock` à mão. **Aceitação:** um teste com 1899 falha antes da mudança; a validação lança erro que menciona `birth_year`; casos válidos continuam passando; Ruff e pytest passam. **Verificação:** execute `uv run pytest`, `uv run ruff check .` e `uv run ruff format --check .`. **Pistas graduais:** (1) compare o teste parametrizado da referência; (2) a condição deve ficar junto da validação de ano; (3) a mensagem precisa ajudar quem usa a CLI. Veja o [spoiler comentado](../solutions/08-modern-python-solution.md) somente depois de tentar.

## Desafio

Sem instalar bibliotecas, crie em sua cópia uma função pura que devolva uma lista ordenada de espécies permitidas. Escreva primeiro dois testes: a lista inclui `dog` e alterar a lista devolvida não modifica `ALLOWED_SPECIES`. Explique por que devolver uma nova lista evita expor a estrutura interna do módulo.

## Se algo deu errado

| Sintoma | Causa provável | Verificação |
| --- | --- | --- |
| `uv: command not found` | uv não está no PATH | siga a instalação oficial, abra novo terminal e rode `uv --version` |
| Python incompatível | runtime abaixo do mínimo do projeto | `uv run python --version`; deixe uv instalar uma versão compatível conforme documentação |
| `ModuleNotFoundError` | sync não ocorreu ou import está errado | `uv sync --all-groups`, confira pacote sob `src/` e nome do import |
| teste não é coletado | arquivo/função não segue convenção pytest | confira `tests/test_*.py` e `test_` |
| traceback longo | erro ocorreu dentro de chamadas encadeadas | leia a última linha primeiro, depois suba até seu arquivo |

## Checkpoint

- [ ] Sei localizar intenção em `pyproject.toml` e resolução em `uv.lock`.
- [ ] Rodei programa, testes e Ruff pelo `uv`.
- [ ] Escrevi um teste que falhou antes de uma mudança de regra.

## Perguntas de reflexão

1. Que problema pode surgir se você instalar uma biblioteca globalmente em vez de declará-la no projeto?
2. Por que `validate_patient` é mais fácil de testar que o comando completo da CLI?
3. Que dado na traceback ajuda a separar erro de import de erro de regra?

## Aprofundamento

Pesquise **“uv lock sync project”**, **“Python src layout packaging”** e **“Python traceback read last line first”**. Leia [uv: projetos e lockfiles](https://docs.astral.sh/uv/concepts/projects/) (essencial), [Python Tutorial: módulos](https://docs.python.org/3/tutorial/modules.html) (essencial) e [Python exceptions](https://docs.python.org/3/tutorial/errors.html) (complementar).

## Resumo

- `uv sync` materializa o ambiente declarado e bloqueado.
- `src/` e módulos deixam responsabilidades legíveis e testáveis.
- Entrada da CLI, regra de negócio e infraestrutura devem ser separadas.
- Traceback é um caminho de investigação, não texto para ignorar.
