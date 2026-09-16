# Preparação no Ubuntu

Estes passos são para Ubuntu nativo ou para o terminal Ubuntu no WSL. Confirme com `uname -a`. `sudo` altera o sistema inteiro: leia a lista proposta e digite a senha somente nesse terminal confiável.

1. Atualize índices e instale Git: `sudo apt update` e `sudo apt install git`. Confirme `git --version`. Não é necessário executar `apt upgrade` para esta trilha; faça atualizações amplas no seu ritmo e após ler a proposta.
2. Instale uv pelo comando da [documentação oficial](https://docs.astral.sh/uv/getting-started/installation/): `curl -LsSf https://astral.sh/uv/install.sh | sh`. Feche e abra o terminal para carregar o `PATH`, depois rode `uv --version` e `python3 --version`. Leia a página antes de executar o instalador; não use `sudo` para uv.
3. Para Node 24 LTS, prefira o pacote Linux x64 ou ARM64 da [página oficial de downloads](https://nodejs.org/en/download), seguindo as instruções fornecidas para sua arquitetura. Após a instalação oficial, abra novo terminal e confirme `node --version` (deve começar por `v24`) e `npm --version`. Evite misturar instalações de Node de fontes diferentes.
4. Instale Docker Engine e o plugin Compose pelo [guia oficial para Ubuntu](https://docs.docker.com/engine/install/ubuntu/). Ele contém comandos com `sudo` e a etapa de pós-instalação; leia especialmente os avisos de privilégios antes de adicionar seu usuário ao grupo `docker`. Confirme `docker version` e `docker compose version`.
5. Instale [VS Code para Linux](https://code.visualstudio.com/docs/setup/linux), abra o clone com `code .` e confirme que o terminal integrado mostra o mesmo `pwd` do terminal externo.

Faça a checagem final: `git --version`, `uv --version`, `python3 --version`, `node --version`, `npm --version`, `docker version` e `docker compose version`. A documentação [Linux command line for beginners](https://documentation.ubuntu.com/desktop/en/26.04/tutorial/the-linux-command-line-for-beginners/) é a referência essencial para os comandos de navegação.
