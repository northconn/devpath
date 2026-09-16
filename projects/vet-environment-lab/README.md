# Vet Environment Lab

Um laboratório pequeno para praticar ambiente de desenvolvimento com um cadastro de pacientes **fictícios**. Os exemplos usam somente dados sintéticos e não oferecem orientação clínica.

O projeto tem duas trilhas:

- `starter/`: ponto de partida para construir por etapas;
- `solution/`: solução de referência, legível e testada.

## Resultado que você vai observar

O primeiro comando mostra uma saudação e informações seguras do ambiente. Na solução, você também poderá validar um paciente fictício, gravá-lo no PostgreSQL, manter um resumo temporário no Redis e diagnosticar os dois serviços.

## Antes de começar

Instale o [uv](https://docs.astral.sh/uv/), o Docker Desktop (ou Docker Engine com o plugin Compose) e Git. Não publique arquivos `.env`: eles podem conter credenciais locais. Este laboratório usa somente credenciais de desenvolvimento, delimitadas ao próprio container.

## Comece pelo starter

```bash
cd starter/python
uv run vet-environment-lab hello
```

Compare a saída com o que você esperava. Ela exibe versão do Python e sistema operacional, mas evita nome de usuário, diretório pessoal, tokens e variáveis de ambiente.

Leia [starter/README.md](starter/README.md) para as tarefas incrementais.

## Execute a solução de referência

Em um terminal, prepare a configuração local e suba os serviços:

```bash
cd solution/infra
cp .env.example .env
docker compose --env-file .env up -d
docker compose --env-file .env ps
```

Espere os dois serviços ficarem `healthy`. As portas são associadas a `127.0.0.1`, portanto só podem ser acessadas desta máquina.

Em outro terminal:

```bash
cd solution/python
uv sync --all-groups
uv run vet-environment-lab hello
uv run vet-environment-lab validate --name "Luna" --species dog --birth-year 2021
uv run vet-environment-lab health
uv run vet-environment-lab add --name "Luna" --species dog --birth-year 2021
uv run vet-environment-lab get --name "Luna"
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

`get` consulta primeiro o Redis. Quando não há um resumo válido no cache, busca o PostgreSQL, que é a fonte de verdade, e repõe o resumo no Redis por 300 segundos.

Para parar os containers sem apagar dados:

```bash
cd ../infra
docker compose --env-file .env down
```

Evite `down --volumes` enquanto quiser conservar os registros locais: esse comando remove o volume nomeado do PostgreSQL.

## Como pedir ajuda

Inclua objetivo, sistema operacional, comando executado, saída completa sem segredos, sua hipótese e o que já tentou. Nunca envie `.env`, tokens, chaves, dados pessoais ou dados clínicos reais. Peça uma pista ou explicação antes de aceitar uma solução; depois confira a documentação oficial e consiga explicar cada alteração.

## Perguntas para conferir entendimento

1. Por que um resumo no Redis não substitui o registro do PostgreSQL?
2. O que mudaria se a porta do PostgreSQL fosse publicada como `0.0.0.0:5432`?
3. Que evidência o comando `health` oferece quando uma credencial está incorreta?
