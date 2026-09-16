# Unidade 4 — Servidores, serviços, virtualização e containers

## Resultado esperado

Você iniciará containers locais, observará portas e logs, explicará imagem versus container e encerrará serviços sem remover dados.

## Tempo estimado

110–155 minutos.

## Pré-requisitos

Unidade 3 e Docker Desktop ou Docker Engine com plugin Compose funcionando (`docker version`).

## Por que isso importa

“Funciona na minha máquina” frequentemente significa dependências instaladas de modos diferentes. Uma configuração declarada permite à equipe iniciar os mesmos serviços e localizar a diferença quando um deles falha.

## Modelo mental

Servidor é um papel: software que responde pedidos, em uma máquina local ou remota. Um serviço é processo de longa duração; daemon é um serviço em segundo plano. Logs contam eventos; configuração e variáveis de ambiente ajustam o processo; a porta recebe conexões. Máquina virtual simula um sistema operacional inteiro sobre hardware virtualizado. Container isola processos usando o sistema operacional do host e parte de uma imagem. Image é receita versionada; container é sua instância em execução. Dockerfile cria imagem; registry a hospeda; tag identifica versão; layer reaproveita etapas. Volume guarda dados fora do ciclo do container, network conecta containers, bind mount compartilha diretório do host. Compose declara vários serviços em um arquivo.

## Vocabulário

| Português | Inglês | Definição |
| --- | --- | --- |
| serviço / daemon | service / daemon | processo persistente que atende trabalho |
| imagem / container | image / container | receita / instância isolada em execução |
| volume | volume | dados persistentes geridos pelo Docker |
| mapeamento de porta | port mapping | ligação entre porta do host e do container |
| log | log | registro de eventos do processo |
| health check | health check | teste automático de disponibilidade do serviço |

## Demonstração guiada

1. Execute `docker run --rm hello-world`. `--rm` remove somente esse container descartável ao fim; a imagem pode continuar localmente.
2. A partir da raiz do repositório, execute `cd projects/vet-environment-lab/solution/infra`, depois `cp .env.example .env` e leia os nomes das variáveis. Os valores são locais de desenvolvimento. No PowerShell, o equivalente é `Copy-Item .env.example .env`.
3. Execute `docker compose --env-file .env up -d` e depois `docker compose --env-file .env ps`. Espere PostgreSQL e Redis em estado `healthy`.
4. Leia, sem editar: `docker compose --env-file .env logs postgres` e `docker compose --env-file .env logs redis`. Logs são evidência; não são senha.
5. Prove o mapeamento de porta com `docker compose --env-file .env port postgres 5432` e `docker compose --env-file .env port redis 6379`. A saída deve apontar para `127.0.0.1:5432` e `127.0.0.1:6379` com os valores padrão. `docker compose --env-file .env ps` prova também que o serviço publicou essa porta e passou no health check.
6. Finalize com `docker compose --env-file .env down`. Este comando para e remove containers/rede, preservando volumes nomeados. **Não use `down --volumes`**: ele remove dados locais persistidos.

## Exercício prático

**Objetivo:** demonstrar o ciclo seguro de um serviço local. **Ponto de partida:** estando em `projects/vet-environment-lab/solution/infra`, use `compose.yaml` e `.env`. **Segurança:** mantenha portas em `127.0.0.1`, use apenas `.env` local e não use `down --volumes`. **Aceitação:** `docker compose --env-file .env ps` mostra serviços saudáveis, você coletou uma linha de log de cada e `docker compose --env-file .env down` terminou sem erro. **Verificação:** rode `docker compose --env-file .env port postgres 5432` antes de parar; depois suba novamente e confira `ps`. **Pistas graduais:** (1) use o mesmo `--env-file`; (2) health check pode levar alguns segundos; (3) `docker compose --env-file .env logs NOME` é mais específico que todos os logs. Veja o [spoiler comentado](../solutions/04-servers-and-containers-solution.md) apenas após tentar.

## Desafio

Sem alterar arquivos, provoque uma falha segura de configuração: estando em `infra/`, execute `POSTGRES_PORT=not-a-port docker compose --env-file .env config`. A configuração deve recusar a porta inválida antes de criar ou alterar containers. Recupere com `unset POSTGRES_PORT` (ou abra outro terminal), execute `docker compose --env-file .env config`, depois `up -d` e `port postgres 5432`. Explique por que a mudança de porta do host não altera a porta interna `5432` do container.

## Se algo deu errado

| Sintoma | Causa provável | Verificação |
| --- | --- | --- |
| Docker não conecta | daemon/Desktop não iniciou | `docker version`; abra Docker Desktop ou serviço oficial |
| porta já em uso | outro listener no host | use ferramenta da Unidade 3; escolha outra porta local no `.env` |
| `unhealthy` | configuração ou inicialização falhou | `docker compose logs NOME` e nomes de variáveis |
| dados parecem sumir | volume não foi usado ou foi removido | leia `compose.yaml`; confirme que não usou `--volumes` |

## Checkpoint

- [ ] Diferencio servidor, serviço, imagem e container.
- [ ] Subi, inspecionei logs e parei o Compose preservando volumes.
- [ ] Sei por que `127.0.0.1` limita o acesso ao computador local.

## Perguntas de reflexão

1. O que se ganha e perde ao usar container em vez de instalar PostgreSQL diretamente no sistema?
2. Que evidência mostraria “imagem foi baixada, mas processo no container falhou”?

## Aprofundamento

Pesquise **“Docker image container difference”**, **“Docker named volume lifecycle”** e **“localhost port mapping”**. Leia [Docker Get Started](https://docs.docker.com/get-started/) (essencial) e procure image, container e volume antes de usar comandos de limpeza.

## Resumo

- Servidor descreve um papel; um serviço é um processo duradouro.
- Imagem é receita, container é execução e volume persiste dados.
- Compose facilita reprodução, mas logs e health checks ainda são sua evidência.
