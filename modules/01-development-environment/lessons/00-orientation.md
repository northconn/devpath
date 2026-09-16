# Unidade 0 — Orientação e primeiro resultado

## Resultado esperado

Você executará o primeiro comando do laboratório, distinguirá terminal de shell e registrará uma evidência sem expor dados pessoais.

## Tempo estimado

45–75 minutos.

## Pré-requisitos

Um terminal aberto e o repositório clonado. Para executar o programa, `uv` instalado conforme seu sistema em [docs](../../../docs/setup-ubuntu.md).

## Por que isso importa

No primeiro dia de uma equipe, o README é a rota para reproduzir o projeto. Uma saída curta e segura prova o estado do ambiente melhor que “acho que instalei tudo”.

## Modelo mental

Um ambiente de desenvolvimento é o conjunto de sistema, ferramentas, configurações e dependências que transforma arquivos em um programa executado. Terminal é a janela; shell é o interpretador de comandos dentro dela; linha de comando é a forma textual de conversar com o shell. `pwd` pergunta onde você está; `ls` mostra o conteúdo daquele diretório.

## Vocabulário

| Português | Inglês | Definição |
| --- | --- | --- |
| ambiente de desenvolvimento | development environment | conjunto de ferramentas para criar e executar software |
| diretório atual | current directory | local em que o shell procura arquivos por padrão |
| comando | command | instrução textual para um programa |

## Demonstração guiada

1. No diretório do repositório, preveja a saída de `pwd` e execute `pwd`. Ela termina em `devpath`.
2. Execute `ls` e localize `projects` e `PROGRESS.md`.
3. Entre no programa inicial: `cd projects/vet-environment-lab/starter/python`.
4. Execute `uv run vet-environment-lab hello`. O `uv` cria/sincroniza o ambiente conforme o lockfile e mostra Python e sistema operacional, sem usuário ou variáveis.
5. Volte ao topo com `cd ../../../..` e confirme com `pwd` seguido de `ls PROGRESS.md`. Marque o primeiro item de [PROGRESS.md](../../../PROGRESS.md). Edite no VS Code ou editor de texto; não cole caminhos pessoais nem a saída completa.

## Exercício prático

**Objetivo:** registrar uma evidência reproduzível do primeiro resultado. **Ponto de partida:** o comando `hello` acima. **Segurança:** use somente a saída do programa; não execute `env`, não copie `.env` e não publique nomes de usuário. **Aceitação:** `PROGRESS.md` contém data, ambiente geral e uma frase sobre a saída. **Verificação:** reabra o arquivo e rode `git diff -- PROGRESS.md`. **Pistas graduais:** (1) a evidência não precisa ser uma captura de tela; (2) descreva “Python e sistema exibidos”; (3) `git diff` mostra somente sua alteração. Depois da tentativa, consulte o [spoiler comentado](../solutions/00-orientation-solution.md).

## Desafio

Sem consultar o arquivo, explique para outra pessoa por que `pwd` pode mudar depois de `cd` e confirme executando os dois comandos.

## Se algo deu errado

| Sintoma | Causa provável | Verificação |
| --- | --- | --- |
| `uv: command not found` | instalação ou `PATH` incompleto | `uv --version` em um novo terminal e guia de setup |
| projeto não encontrado | diretório atual errado | `pwd` e `ls projects` no topo |
| erro de dependência | sincronização interrompida | execute novamente `uv run ...` e leia a primeira mensagem de erro |

## Checkpoint

- [ ] Sei apontar terminal, shell e diretório atual.
- [ ] Executei `hello` e deixei uma evidência segura no progresso.

## Perguntas de reflexão

1. Que evidência diferenciaria “o programa não existe” de “estou no diretório errado”?
2. Por que uma saída com nome de usuário ajuda pouco a reproduzir um problema e pode criar risco?

## Aprofundamento

Pesquise **“shell versus terminal”** para diferenciar interface e interpretador; **“uv project sync lockfile”** para descobrir por que dependências são reproduzíveis; leia [uv projects](https://docs.astral.sh/uv/concepts/projects/sync/) (essencial) e identifique o que `uv.lock` fixa.

## Resumo

- O diretório atual muda o significado de caminhos relativos.
- Terminal, shell e comando são partes diferentes do mesmo fluxo.
- A primeira execução deve gerar uma evidência útil e segura.
