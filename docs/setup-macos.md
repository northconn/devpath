# Preparação no macOS

Abra **Terminal** (normalmente `zsh`), clone o repositório em sua pasta pessoal e confirme `pwd`. Todos os comandos desta página rodam nesse terminal; não use `sudo` para instalar ferramentas no diretório do projeto.

1. Instale as Command Line Tools da Apple com `xcode-select --install`; elas incluem Git. Quando o diálogo terminar, confirme `git --version`. Leia [documentação Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) se o macOS já tiver uma versão ou pedir atualização.
2. Instale uv pelo comando da [página oficial de instalação](https://docs.astral.sh/uv/getting-started/installation/): `curl -LsSf https://astral.sh/uv/install.sh | sh`. Feche e reabra o Terminal, então confirme `uv --version` e `python3 --version`. Leia o script/documentação antes de executá-lo; ele altera somente a instalação do uv e o perfil do shell, não requer `sudo`.
3. Baixe e execute o instalador **macOS Installer (.pkg)** de Node 24 LTS na [página de downloads oficial do Node](https://nodejs.org/en/download). Reabra o Terminal e confirme `node --version` e `npm --version`.
4. Instale [Docker Desktop para Mac](https://docs.docker.com/desktop/setup/install/mac-install/) seguindo o pacote correto para Apple silicon ou Intel. Abra o aplicativo e aguarde iniciar; confirme `docker version` e `docker compose version` no Terminal.
5. Instale [VS Code para macOS](https://code.visualstudio.com/docs/setup/mac), abra a pasta clonada em **File → Open Folder**, e só então instale extensões mínimas conforme o módulo.

Se uma instalação solicitar senha, identifique qual pacote a solicita e leia a tela antes de aceitar. Não copie saída que revele caminhos pessoais, chaves ou tokens ao pedir ajuda.
