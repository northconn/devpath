# Unidade 7 — Git, GitHub e o primeiro repositório

## Resultado esperado

Você criará uma branch para uma mudança pequena, revisará o diff, resolverá um conflito preparado e saberá preparar uma issue e um pull request (PR) sem expor segredos.

## Tempo estimado

130–180 minutos.

## Pré-requisitos

Unidade 6 e uma conta GitHub criada ou acesso a um repositório de prática.

## Por que isso importa

Quando duas pessoas editam o mesmo arquivo, Git preserva as duas histórias até alguém decidir como combiná-las. Um commit pequeno, uma issue com contexto e um PR revisável deixam essa decisão visível e recuperável.

## Modelo mental

Git registra versões locais. O diretório de trabalho contém suas alterações; a **staging area** (índice) escolhe o que entra no próximo commit; um commit é um retrato nomeado e com autor. GitHub hospeda um repositório remoto e oferece issues, PRs e CI. `origin` é só o nome convencional desse remoto. Branch é uma linha de trabalho apontando para commits; não é uma cópia solta de arquivos.

GitHub não aceita senha da conta como autenticação Git por HTTPS. Prefira Git Credential Manager ou SSH com chave protegida por passphrase, seguindo a [documentação oficial](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure). Use senha única e autenticação multifator (MFA). Nunca ponha token em URL, README, `.env` versionado ou captura de tela.

## Vocabulário

| Português | Inglês | Definição |
| --- | --- | --- |
| área de preparação | staging area / index | seleção para o próximo commit |
| confirmação | commit | registro local de uma alteração coerente |
| remoto | remote | repositório acessível por URL |
| ramificação | branch | nome que aponta para uma linha de commits |
| solicitação de mudança | pull request | proposta para revisar e integrar uma branch |
| conflito | merge conflict | trecho que Git não consegue combinar sozinho |

## Demonstração guiada

1. Instale Git pelo [site oficial](https://git-scm.com/downloads) e confira `git --version`. Configure autoria, usando e-mail que você decidiu associar aos commits: `git config --global user.name "Seu Nome"` e `git config --global user.email "seu-email@example.com"`. Confira com `git config --global --get-regexp '^user\.'`. Isso não configura login no GitHub.
2. Crie a conta no GitHub com senha única e ative MFA em **Settings > Password and authentication**. Configure HTTPS por Git Credential Manager ou uma chave SSH conforme [Connecting to GitHub with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh); aceite o login no navegador, nunca copie um token para o repositório.
3. Na raiz deste repositório, leia primeiro `git status` e `git log --oneline -5`. Em seu clone pessoal, crie uma branch: `git switch -c docs/git-lab-note`. Branches usam nomes descritivos e não devem começar com dado sensível.
4. Crie uma nota local fora de arquivos sensíveis, por exemplo `notes/git-lab.md`, com uma frase sobre o comando `hello`. Use o editor. Em seguida, execute `git diff`, `git status`, `git add notes/git-lab.md`, `git diff --staged` e `git commit -m "docs: add Git lab note"`. Cada comando responde a uma pergunta diferente: o que mudou, o que será commitado e o que foi registrado.
5. Se o remoto já existe, confirme antes com `git remote -v`, envie `git push -u origin docs/git-lab-note`, abra uma issue que descreva objetivo, reprodução e evidências, e crie PR da branch para a branch padrão. Revise **Files changed**, cite testes executados e confirme que nenhum `.env` aparece.
6. Para praticar conflito sem tocar no laboratório, em uma cópia temporária fora do repositório execute:

   ```bash
   mkdir -p /tmp/vet-git-conflict-lab
   cd /tmp/vet-git-conflict-lab
   git init
   git config user.name "Student"
   git config user.email "student@example.invalid"
   printf 'cache_ttl_seconds=300\n' > settings.txt
   git add settings.txt
   git commit -m "chore: add cache setting"
   git switch -c docs-explanation
   printf 'cache_ttl_seconds=300 # temporary cache\n' > settings.txt
   git commit -am "docs: explain cache setting"
   git switch -
   printf 'cache_ttl_seconds=120\n' > settings.txt
   git commit -am "feat: shorten cache TTL"
   git merge docs-explanation
   ```

   Git marca conflito porque as duas versões editam a mesma linha. Abra `settings.txt`, preserve uma decisão consciente, por exemplo `cache_ttl_seconds=120 # temporary cache`, remova marcadores `<<<<<<<`, `=======`, `>>>>>>>`, então rode `git add settings.txt`, `git commit -m "merge: resolve cache setting conflict"` e `git log --oneline --graph --all`. Não use `reset --hard`, `push --force` ou exclusão de histórico como atalho.

## Exercício prático

**Objetivo:** publicar uma alteração documental revisável do laboratório. **Ponto de partida:** seu fork ou repositório próprio e uma branch atualizada da branch padrão. **Segurança:** confira `git status` e `git diff --staged` antes de cada commit; nunca adicione `.env`, token, chave SSH ou dados reais. **Aceitação:** issue com objetivo e evidência; branch com nome descritivo; pelo menos um commit em inglês no imperativo; PR que liga a issue, descreve testes e não inclui segredo. **Verificação:** no PR, compare a aba Files changed com `git diff` local e confirme CI verde quando o repositório tiver workflow. **Pistas graduais:** (1) `git status` diz o próximo comando seguro; (2) `git diff --staged` é a revisão antes do commit; (3) o PR pode ser aberto como rascunho. Veja o [spoiler comentado](../solutions/07-git-and-github-solution.md) depois de tentar.

## Desafio

Na cópia temporária, faça o conflito de `settings.txt` e resolva-o mantendo `120` e a explicação. Explique por que Git não escolhe automaticamente uma das linhas: ambas podem representar intenção válida da equipe. Registre o hash do merge, não o conteúdo de credenciais.

## Se algo deu errado

| Sintoma | Causa provável | Verificação |
| --- | --- | --- |
| `Author identity unknown` | nome/e-mail não configurados | `git config --get user.name` e `git config --get user.email` |
| push pede senha e falha | método de autenticação inadequado | use Credential Manager, token inserido apenas no prompt ou SSH; leia a documentação GitHub |
| arquivo errado entrou no staging | `git add .` amplo demais | `git restore --staged caminho/do/arquivo`, depois revise |
| conflito possui marcadores | edição concorrente na mesma região | leia as duas intenções, edite resultado, `git add` e commit |
| branch está atrás do remoto | outra pessoa publicou commits | `git fetch origin`, revise e use `git pull` conscientemente |

## Checkpoint

- [ ] Distingo diretório de trabalho, staging, commit e remoto.
- [ ] Configurei uma forma segura de autenticação e MFA na conta.
- [ ] Revisei um diff e resolvi um conflito pequeno sem reescrever histórico.

## Perguntas de reflexão

1. Que informação em um commit ajuda uma pessoa a revisar a mudança depois?
2. Qual é a diferença entre autoria de commit e autenticação no GitHub?
3. Que evidência incluiria numa issue para separar falha local de falha na CI?

## Aprofundamento

Pesquise **“Git staging area index explanation”**, **“GitHub SSH key passphrase”** e **“Git merge conflict markers”**. Leia [Pro Git: Git Branching](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell) (essencial), [GitHub Hello World](https://docs.github.com/en/get-started/start-your-journey/hello-world) (essencial) e [sobre repositórios remotos](https://docs.github.com/en/get-started/git-basics/about-remote-repositories) (complementar).

## Resumo

- Git registra trabalho local; GitHub é um remoto e espaço de colaboração.
- Staging deliberado e revisão do diff previnem commits acidentais.
- MFA e autenticação por ferramenta oficial protegem conta e repositório.
- Conflito pede decisão sobre intenção, seguida de teste e commit.
