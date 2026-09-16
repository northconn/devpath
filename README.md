# DevPath — Módulo 1: Ambiente de desenvolvimento

Uma trilha prática, em português brasileiro, para preparar um ambiente de desenvolvimento e entender o que ele faz. Você construirá o **Vet Environment Lab**, um cadastro de pacientes animais inteiramente fictícios: um programa Python modular, testes, PostgreSQL, Redis em containers e uma pequena comparação em TypeScript. Não há dados reais nem orientação clínica.

## Comece agora: Unidade 0

Abra [a Unidade 0](modules/01-development-environment/lessons/00-orientation.md), siga a demonstração e marque a primeira evidência em [PROGRESS.md](PROGRESS.md). É o único ponto de partida necessário.

## Ao final, você terá construído

- um ambiente verificável com terminal, Git, VS Code, Python/uv, Node.js e Docker;
- o laboratório executando, testado e organizado em módulos;
- PostgreSQL como fonte de verdade e Redis como cache temporário, ambos locais;
- evidências de diagnóstico, qualidade e um fluxo inicial de Git/GitHub.

## Navegação

- [Trilha e ordem sugerida](docs/learning-path.md)
- [Glossário](docs/glossary.md) e [versões das ferramentas](docs/tooling-versions.md)
- Instalação: [Windows + WSL2](docs/setup-windows-wsl.md), [macOS](docs/setup-macos.md), [Ubuntu](docs/setup-ubuntu.md)
- [Projeto integrador](projects/vet-environment-lab/README.md)
- [Guia para contribuir](CONTRIBUTING.md) e [conduta](CODE_OF_CONDUCT.md)

## Regra de segurança

Nunca publique `.env`, tokens, chaves, nomes de usuário, caminhos pessoais ou dados de pacientes reais. Os exemplos do repositório usam somente informação sintética e serviços acessíveis em `127.0.0.1`.
