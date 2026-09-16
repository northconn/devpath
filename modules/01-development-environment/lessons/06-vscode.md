# Unidade 6 — VS Code e ferramentas de desenvolvimento

## Resultado esperado

Você abrirá o Vet Environment Lab como *workspace*, escolherá o interpretador criado pelo `uv` e localizará a causa de um bug preparado com breakpoint e *stack trace*.

## Tempo estimado

90–130 minutos.

## Pré-requisitos

Unidades 0–5; `uv` instalado; a cópia do repositório disponível localmente.

## Por que isso importa

Um relato útil de bug diz como reproduzir, qual entrada foi usada, qual arquivo e linha aparecem no erro e qual hipótese foi testada. Isso permite que outra pessoa investigue sem receber credenciais ou uma captura incompleta.

## Modelo mental

O VS Code é um editor que reúne arquivos, terminal, diagnóstico e controle de versão; ele não substitui Python, `uv` ou Git. Um *workspace* é a pasta que o editor trata como projeto. Configurações de usuário valem para todos os projetos; configurações do workspace ficam no projeto e só devem existir quando a equipe precisa delas. Antes de confiar em código baixado, confirme o **Workspace Trust**: tarefas, extensões e configurações podem executar comandos.

O depurador pausa um processo. Um **breakpoint** marca a pausa; *step over* executa a próxima linha sem entrar na função chamada; *step into* entra nela; a *stack trace* mostra a sequência de chamadas até o erro. Variáveis inspecionadas são evidência do estado naquele instante, não uma explicação sozinha.

## Vocabulário

| Português | Inglês | Definição |
| --- | --- | --- |
| área de trabalho | workspace | pasta e configurações abertas como projeto |
| interpretador | interpreter | programa que executa Python |
| ponto de parada | breakpoint | local em que o depurador pausa |
| pilha de chamadas | stack trace | caminho de funções até a falha |
| painel de problemas | Problems panel | diagnósticos de ferramentas do editor |
| confiança do workspace | Workspace Trust | decisão de permitir automações daquele código |

## Demonstração guiada

1. Instale a versão estável pelo [guia oficial](https://code.visualstudio.com/docs/getstarted/overview). No Ubuntu/macOS, abra a raiz com `code .` se o comando estiver disponível; no Windows, abra a pasta pela interface ou pelo VS Code conectado ao WSL.
2. Abra `projects/vet-environment-lab/solution/python` como pasta. Leia o aviso de confiança antes de aceitar. Abra o terminal integrado em **Terminal > New Terminal** e execute `uv sync --all-groups`.
3. Selecione **Python: Select Interpreter** na Command Palette (`Ctrl+Shift+P` ou `Cmd+Shift+P`) e escolha o Python sob `.venv`. Confirme no terminal integrado com `uv run python --version`. Não selecione Python global só porque aparece primeiro.
4. Instale apenas extensões que ajudam este laboratório: **Python** (Microsoft), **Ruff** (Astral) e, quando usar a Unidade 9, **ESLint**. No Windows com WSL, instale também **WSL** (Microsoft); para inspecionar serviços, **Docker** (Microsoft). Extensões executam código: confira editora, permissões e necessidade.
5. Abra `src/vet_environment_lab/validation.py`. Antes de rodar, preveja: `validate_patient(" ", "dog", 2021)` normaliza o nome para vazio e gera `ValidationError`.
6. Clique à esquerda da linha `normalized_name = name.strip()` para criar um breakpoint. Como `validation.py` só define funções, use a CLI real: abra **Run and Debug**, escolha **create a launch.json file**, selecione **Python Debugger** e crie a configuração abaixo em `.vscode/launch.json` dentro de `solution/python`:

   ```json
   {
     "version": "0.2.0",
     "configurations": [
       {
         "name": "Debug fictional patient validation",
         "type": "debugpy",
         "request": "launch",
         "module": "vet_environment_lab.cli",
         "args": ["validate", "--name", " ", "--species", "dog", "--birth-year", "2021"],
         "console": "integratedTerminal",
         "justMyCode": true
       }
     ]
   }
   ```

   Selecione `Debug fictional patient validation` e pressione F5. O módulo e os argumentos são os mesmos usados por `uv run vet-environment-lab validate --name " " --species dog --birth-year 2021`; o interpretador `.venv` selecionado na etapa 3 fornece as dependências. Pare na linha, inspecione `name` e use step over. A saída normal é `Invalid fictional patient`: a regra de nome aponta para entrada inválida, não para Docker.
7. Abra o painel Problems; ele mostra diagnósticos estáticos, que podem ser diferentes de um erro em execução. Confirme que a configuração usa `vet_environment_lab.cli`, não `validation.py`: a CLI chama a função e permite observar a stack trace inteira.
8. Para praticar uma falha preparada, substitua temporariamente a linha exata `normalized_name = name.strip()` por `normalized_name = name.strip().lowercase()` e **salve** o arquivo. Mantenha o breakpoint nessa linha e pressione F5 na configuração criada. Inspecione `name`, avance até `AttributeError` e leia a stack trace. Restaure a linha exata `normalized_name = name.strip()`, salve e pressione F5 de novo; a execução volta a terminar com a mensagem de validação esperada. `str` em Python não possui `lowercase`; `lower()` existe, mas não é necessário para normalizar o nome neste código. Não faça commit dessa alteração nem de `launch.json` sem acordo da equipe.

## Exercício prático

**Objetivo:** produzir uma nota de diagnóstico do bug preparado. **Ponto de partida:** `solution/python` sincronizado, `validation.py` aberto e a configuração `Debug fictional patient validation` criada. **Segurança:** use apenas entrada fictícia; não cole `.env`, caminhos pessoais, tokens ou a saída de variáveis de ambiente na nota. **Aceitação:** a nota contém a configuração/argumentos de reprodução, erro completo, arquivo/linha, valor observado de `name`, causa (`lowercase` não existe em `str`) e a restauração da linha original `normalized_name = name.strip()`. **Verificação:** com o arquivo restaurado, F5 termina em mensagem de validação de nome; `uv run vet-environment-lab validate --name "  LUNA  " --species DOG --birth-year 2021` imprime JSON com `"name": "LUNA"` e `"species": "dog"`. **Pistas graduais:** (1) o painel Run and Debug mostra Call Stack; (2) diferencie o valor de `name` do valor após `strip`; (3) compare o nome do método com a documentação de `str`. Veja o [spoiler comentado](../solutions/06-vscode-solution.md) depois de tentar.

## Desafio

Abra `src/vet_environment_lab/cli.py`, ponha um breakpoint no bloco `elif args.command == "validate"` e execute uma validação válida. Sem alterar a regra, explique em uma frase por que `Settings()` é criado antes de saber que o comando é `validate` e por que isso ainda não abre conexão com PostgreSQL ou Redis. Use a stack trace e a leitura de `config.py` como evidência.

## Se algo deu errado

| Sintoma | Causa provável | Verificação |
| --- | --- | --- |
| `code: command not found` | comando não entrou no PATH | abra pela interface; no macOS execute o comando de instalação do PATH na Command Palette |
| import não encontrado no editor | interpretador global selecionado | escolha `.venv` e execute `uv sync --all-groups` |
| breakpoint fica vazio | processo iniciou fora do depurador | use Run and Debug, não só o terminal |
| `AttributeError` inesperado | nome de método ou tipo diferente do previsto | leia a linha e o tipo mostrado pelo depurador |
| arquivos parecem confiáveis mas são desconhecidos | pasta aberta sem revisão | mantenha Restricted Mode até ler README e configurações |

## Checkpoint

- [ ] Abri a pasta Python como workspace e selecionei `.venv`.
- [ ] Expliquei breakpoint, step over e stack trace com uma observação real.
- [ ] Reproduzi, diagnostiquei e reverti o bug preparado.

## Perguntas de reflexão

1. Qual evidência diferenciaria uma regra de validação errada de um interpretador errado?
2. Por que uma configuração do workspace merece revisão de quem faz clone?
3. Como você relataria o bug sem anexar o arquivo `.env`?

## Aprofundamento

Pesquise **“VS Code Python select interpreter virtual environment”** para entender como a extensão encontra `.venv`; **“VS Code debugger call stack step over”** para comparar pausas e chamadas; e **“Python str lower documentation”** para confirmar a API. Leia [Getting Started with VS Code](https://code.visualstudio.com/docs/getstarted/overview) (essencial), [Python debugging no VS Code](https://code.visualstudio.com/docs/python/debugging) (essencial) e [Workspace Trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust) (complementar).

## Resumo

- Editor, runtime e ferramentas de qualidade são componentes distintos.
- O interpretador `.venv` torna a execução coerente com o lockfile.
- Breakpoint e stack trace transformam uma hipótese em evidência.
- Confiança de workspace é uma decisão de segurança.
