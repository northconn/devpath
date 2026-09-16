# Unidade 2 — Windows, macOS e Linux

## Resultado esperado

Você navegará e manipulará uma árvore de arquivos de laboratório com segurança e identificará em qual sistema um comando está sendo executado.

## Tempo estimado

90–130 minutos.

## Pré-requisitos

Unidades 0 e 1, e o guia de instalação do seu sistema.

## Por que isso importa

Um README pode pedir `ls`, um comando Linux, enquanto a pessoa está em PowerShell. Reconhecer o ambiente evita adaptar comandos às cegas e produzir arquivos no local errado.

## Modelo mental

Todo sistema operacional organiza processos, arquivos, rede, usuários e instalações, mas oferece interfaces diferentes. Windows usa PowerShell e caminhos como `C:\`; macOS e Linux usam shells como `zsh`/`bash` e caminhos `/`. Linux é o kernel; uma distribuição junta kernel, ferramentas e gerenciador de pacotes. Debian e Ubuntu são uma família prática aqui. WSL2 executa Linux integrado ao Windows, mas ainda há filesystem, ferramentas e configurações distintos. `sudo` eleva privilégio: use-o apenas quando uma documentação confiável explicar a alteração.

## Vocabulário

| Português | Inglês | Definição |
| --- | --- | --- |
| sistema operacional | operating system | software que administra o computador |
| distribuição | distribution | sistema Linux empacotado para uso |
| privilégio | privilege | autorização para ação administrativa |
| copiar / mover | copy / move | duplicar / transferir arquivo |
| remover | remove | apagar um alvo explícito |

## Demonstração guiada

1. Identifique o ambiente: Linux/WSL `uname -s`; macOS `sw_vers`; PowerShell `$PSVersionTable.PSVersion`. No WSL, `uname -a` menciona Microsoft.
2. Em Linux/macOS, crie uma área segura: `mkdir -p /tmp/devpath-files/{notes,data}`. No PowerShell: `New-Item -ItemType Directory -Force "$env:TEMP\devpath-files\notes"` e equivalente para `data`.
3. Linux/macOS: `printf 'synthetic\n' > /tmp/devpath-files/notes/readme.txt`, `cp .../readme.txt .../data/copy.txt`, `mv .../copy.txt .../data/renamed.txt`, `cat .../renamed.txt`. PowerShell: `Set-Content`, `Copy-Item`, `Move-Item`, `Get-Content` nos caminhos equivalentes.
4. Busque texto: Linux/macOS `rg synthetic /tmp/devpath-files`; PowerShell `Select-String -Path "$env:TEMP\devpath-files\*\*" -Pattern synthetic`.
5. Antes de apagar, liste o alvo. Linux/macOS: `ls /tmp/devpath-files/data` e `rm /tmp/devpath-files/data/renamed.txt`; PowerShell: `Get-ChildItem` e `Remove-Item` com caminho explícito. Nunca use remoção recursiva como prática.

## Exercício prático

**Objetivo:** criar `draft`, `review` e `published` em uma árvore temporária e mover um arquivo entre elas. **Ponto de partida:** `/tmp/devpath-files` ou `$env:TEMP\devpath-files`. **Segurança:** trabalhe somente nesse diretório e liste antes de remover qualquer arquivo. **Aceitação:** há um arquivo com “synthetic” em `published` e nenhum em `draft`. **Verificação:** liste a árvore e busque o texto. **Pistas graduais:** (1) crie diretórios antes do arquivo; (2) use cópia somente se quiser duas versões; (3) caminho com espaço exige aspas. A resposta está no [spoiler comentado](../solutions/02-operating-systems-solution.md).

## Desafio

Um README diz `cp .env.example .env`. Explique por que ele funciona em bash/zsh, por que não é um comando PowerShell padrão e como você encontraria a alternativa na ajuda local.

## Se algo deu errado

| Sintoma | Causa provável | Verificação |
| --- | --- | --- |
| `No such file` | caminho relativo partiu do local errado | `pwd` ou `Get-Location`; use caminho absoluto temporário |
| acesso negado | alvo fora da área do aluno | volte à pasta temporária; não aplique `sudo` |
| comando Linux no PowerShell falha | shell diferente | confirme a janela e procure `Get-Help COMANDO` |

## Checkpoint

- [ ] Sei distinguir Windows, macOS, Linux e WSL2 no contexto do terminal.
- [ ] Criei, copiei, movi, busquei e removi um arquivo de alvo explícito.

## Perguntas de reflexão

1. Que evidência mostraria que o arquivo existe no Windows, mas não no filesystem Linux do WSL?
2. O que se ganha ao pedir privilégio somente para uma ação delimitada?

## Aprofundamento

Pesquise **“WSL file system performance project folder”**, **“Debian Ubuntu distribution difference”** e **“PowerShell Get-Help examples”**. Leia [instalação WSL](https://learn.microsoft.com/en-us/windows/wsl/install) (essencial) para descobrir limites e requisitos.

## Resumo

- Sistemas compartilham responsabilidades, mas shells e caminhos diferem.
- WSL integra ambientes sem eliminá-los.
- Liste o alvo antes de alterar ou remover arquivos.
