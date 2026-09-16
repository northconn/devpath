# Preparação no Windows com WSL2

## Contexto correto

Abra **PowerShell como administrador** apenas para instalar WSL: `wsl --install`. Reinicie se solicitado. Abra Ubuntu pelo menu e crie a conta Linux; os comandos seguintes rodam no terminal **Ubuntu**, não no PowerShell. `uname -a` identifica o Linux/WSL; `pwd` deve mostrar `/home/...`. Windows e WSL são integrados, mas continuam ambientes diferentes.

## Ferramentas

1. No Ubuntu do WSL, siga as etapas de Git, uv e Node da página [Ubuntu](setup-ubuntu.md). Feche e abra o Ubuntu depois de instalar uv ou Node para o shell reler o `PATH`.
2. Instale [Docker Desktop para Windows](https://docs.docker.com/desktop/setup/install/windows-install/) (essencial). Nas configurações, habilite **Use the WSL 2 based engine** e a integração com sua distribuição Ubuntu. Então, no Ubuntu, execute `docker version` e `docker compose version`. Não instale um segundo daemon Docker dentro do WSL sem entender qual deles atenderá o comando.
3. Instale [VS Code](https://code.visualstudio.com/docs/setup/windows) (essencial) no Windows e a extensão **WSL**. Do Ubuntu, em `~/devpath`, execute `code .`; a indicação WSL no canto inferior esquerdo confirma que extensões e terminal pertencem ao Linux.
4. Confirme no Ubuntu: `git --version`, `uv --version`, `python3 --version`, `node --version`, `npm --version`, `docker version` e `docker compose version`.

Fontes: [instalação oficial do WSL](https://learn.microsoft.com/en-us/windows/wsl/install) (essencial) e [VS Code + WSL](https://code.visualstudio.com/docs/remote/wsl) (essencial). Mantenha o clone em `~/` do WSL para ferramentas Linux consistentes; `explorer.exe .` abre essa pasta no Windows. Não copie o projeto entre `C:` e Linux a cada comando.
