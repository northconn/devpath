# Unidade 1 — Como o computador executa trabalho

## Resultado esperado

Você explicará as camadas entre um arquivo e sua execução e observará processo, recursos, arquivos e `PATH` com comandos seguros.

## Tempo estimado

75–110 minutos.

## Pré-requisitos

Unidade 0 concluída e um terminal no repositório.

## Por que isso importa

Quando uma CI encontra uma ferramenta ausente ou um computador fica lento, a equipe precisa de observações: qual processo, qual memória, qual caminho de busca. “Meu computador travou” não orienta uma correção.

## Modelo mental

Hardware executa instruções: CPU (central processing unit) tem núcleos que fazem trabalho; RAM é memória rápida e temporária; disco persiste arquivos. Bits são zeros e uns; oito bits formam um byte. O sistema operacional administra recursos. Um runtime, como Python, interpreta ou executa o código da aplicação. Ao iniciar um programa, o sistema cria um processo; threads são fluxos de trabalho dentro desse processo. RAM cheia pode deixar o sistema lento ou encerrar processos; espaço em disco cheio impede persistir arquivos. Caminho absoluto começa na raiz; relativo parte do diretório atual. `PATH` lista diretórios onde o shell busca comandos.

## Vocabulário

| Português | Inglês | Definição |
| --- | --- | --- |
| CPU / núcleo | CPU / core | processador e unidade que executa instruções |
| memória RAM | RAM | memória temporária de programas ativos |
| armazenamento | storage | disco persistente |
| processo / thread | process / thread | programa em execução / fluxo dentro dele |
| permissão | permission | regra de acesso a arquivo ou diretório |
| caminho de busca | PATH | diretórios consultados para achar comandos |

## Demonstração guiada

1. Preveja se `command -v python` mostra um caminho ou nada; execute-o. Ele consulta o `PATH`, não procura o disco inteiro.
2. Execute `printf '%s\n' "$PATH"`; leia apenas os diretórios, sem publicar a saída se ela contiver caminho pessoal.
3. Linux/WSL: `ps -eo pid,comm,%cpu,%mem --sort=-%mem | head`. macOS: `ps -Ao pid,comm,%cpu,%mem -r | head`. Veja identificador (PID), nome e uso aproximado.
4. Linux/WSL: `free -h`; macOS: `vm_stat`. Veja que formatos variam, mas ambos observam memória.
5. Execute `ls -l README.md`; a primeira coluna mostra permissões. Não altere permissões nesta lição.

## Exercício prático

**Objetivo:** investigar um comando “não encontrado” sem instalar nada. **Ponto de partida:** escolha `python`, `uv` ou `git`. **Segurança:** não use `sudo`, não altere `PATH` e não encerre processos. **Aceitação:** registre qual comando foi escolhido, resultado de `command -v` e uma hipótese se não for encontrado. **Verificação:** repita `COMANDO --version` quando houver caminho. **Pistas graduais:** (1) `command -v` usa o shell; (2) caminho encontrado não garante versão compatível; (3) compare com [tooling versions](../../../docs/tooling-versions.md). Consulte o [spoiler comentado](../solutions/01-how-computers-work-solution.md) somente após registrar sua hipótese.

## Desafio

Explique a diferença entre remover um arquivo e encerrar um processo. Que evidência você procuraria antes de agir em cada caso?

## Se algo deu errado

| Sintoma | Causa provável | Verificação |
| --- | --- | --- |
| `command -v` vazio | programa ausente ou `PATH` não o inclui | abra novo terminal; consulte instalação oficial |
| `ps` parece confuso | saída tem muitas colunas | leia PID, comando, CPU e memória primeiro |
| sem permissão para arquivo | regras do sistema | confira `ls -l`; não use `sudo` como atalho |

## Checkpoint

- [ ] Consigo desenhar hardware → sistema operacional → runtime → aplicação.
- [ ] Observei processo e recursos sem interromper nada.
- [ ] Sei que `PATH` explica muitos “command not found”.

## Perguntas de reflexão

1. Que evidência separa falta de RAM de falta de espaço em disco?
2. Por que dois processos do mesmo programa podem ter PIDs diferentes?

## Aprofundamento

Pesquise **“process versus thread”** e **“absolute relative path shell”**; procure **“Unix file permissions rwx”** para descobrir quem pode ler, escrever ou executar. Consulte a seção de linha de comando do [Ubuntu](https://documentation.ubuntu.com/desktop/en/26.04/tutorial/the-linux-command-line-for-beginners/) (complementar) para exemplos seguros.

## Resumo

- Software usa hardware por meio do sistema operacional.
- RAM é temporária; armazenamento persiste.
- Processo, arquivo e `PATH` são evidências distintas de diagnóstico.
