# Spoiler — Unidade 3

## Resposta trabalhada

Um relatório útil é: “`nslookup example.com` resolveu um IP. `curl -I --max-time 5 https://example.com` recebeu um status HTTP. DNS, conexão e resposta HTTP funcionaram neste momento.” O relatório não inclui cookies, cabeçalhos sensíveis, IP da rede interna ou credenciais.

Nome sem resolução pede conferir grafia, rede e resolvedor DNS. `connection refused` indica que chegou ao host, mas nenhuma aplicação aceitou aquela porta. Timeout não recebeu resposta no prazo e pede investigar rota, firewall ou serviço. HTTP 401/403 é uma resposta da aplicação: identidade ou autorização precisa ser revista. Essas classes são diferentes; desativar firewall ou tentar senhas não é diagnóstico e cria risco.
