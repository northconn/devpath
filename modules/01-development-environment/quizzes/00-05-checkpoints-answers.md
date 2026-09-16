# Gabarito comentado — Checkpoints das Unidades 0–5

1. **B, `command -v NOME`.** Ele pergunta ao shell se o nome está disponível no `PATH`. Apagar cache não corrige ausência de executável; `sudo` muda privilégios sem explicar o problema; encerrar processos não influencia a busca do shell.
2. Prova que Compose publicou a porta interna 5432 em `127.0.0.1:5432` no host. Não prova que PostgreSQL aceita autenticação ou que a aplicação usa a credencial correta; `ps`, health check e `uv run vet-environment-lab health` tratam essas evidências.
3. **B, volume.** Imagem é a receita usada para criar containers. Log é registro transitório e tag é um nome de versão de imagem. O volume foi criado para sobreviver ao ciclo do container.
4. Para receber HTTP 404, o nome precisou ser resolvido e a conexão/TLS precisou avançar o suficiente para receber resposta. A hipótese é que o servidor está ativo, mas a rota ou recurso pedido não existe; não é a mesma evidência de DNS falho ou timeout.
5. PostgreSQL continua fonte de verdade. A aplicação pode buscar o banco e avisar que cache está indisponível, em vez de inventar ou perder o dado. Registre saída de `health`, estado de `docker compose ps redis` e log do Redis, omitindo `.env` e senhas.
