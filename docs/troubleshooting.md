# Diagnóstico inicial

| Sintoma | Hipóteses | Verificação segura |
| --- | --- | --- |
| `command not found` | ferramenta ausente ou fora do `PATH` | `command -v NOME`, depois `NOME --version` |
| porta em uso | outro processo já escuta | Linux: `ss -ltnp`; macOS: `lsof -nP -iTCP:PORT -sTCP:LISTEN` |
| conexão recusada | host respondeu, mas serviço não aceita a porta | `docker compose ps`, logs do serviço e porta configurada |
| timeout | rota, firewall ou serviço não responde | tente `curl --max-time 5 URL`; confira host e rede |
| credencial falha | variável ausente ou valor não coincide | confira nomes no `.env.example`, sem publicar `.env` |
| container unhealthy | processo interno falhou | `docker compose logs NOME`; não remova volume para "tentar de novo" |

Ao pedir ajuda, informe objetivo, sistema operacional, comando, saída completa sem segredos, hipótese e tentativa anterior. Uma boa primeira pergunta a uma IA é: “faça três perguntas para eu investigar esta saída antes de sugerir comandos”. Confira a explicação na documentação oficial e só execute um comando que você compreende.
