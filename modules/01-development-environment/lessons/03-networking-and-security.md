# Unidade 3 — Redes, protocolos e segurança básica

## Resultado esperado

Você descreverá uma requisição simples e distinguirá falha de DNS, recusa de conexão, timeout e erro HTTP usando ferramentas não intrusivas.

## Tempo estimado

100–140 minutos.

## Pré-requisitos

Unidade 2 e acesso à internet para os exemplos públicos.

## Por que isso importa

“A API caiu” pode significar nome sem resolução, serviço em porta errada, firewall, credencial ou resposta HTTP. A equipe economiza tempo quando o relato identifica a camada e a evidência.

## Modelo mental

Uma rede local conecta máquinas; a internet conecta redes. Cliente pede, servidor responde. Um hostname como `example.com` vira endereço IP pelo DNS (Domain Name System). `localhost` é a própria máquina; porta separa serviços no mesmo IP; socket é a combinação prática de endereço, porta e protocolo. O modelo OSI serve como mapa; no trabalho, TCP/IP é mais usado: enlace (Ethernet/Wi-Fi), internet (IP), transporte (TCP/UDP) e aplicação (HTTP, DNS). TCP prioriza entrega ordenada; UDP reduz coordenação. HTTPS é HTTP protegido por TLS. SSH abre uma sessão remota autenticada. Autenticação prova quem é você; autorização define o que pode fazer. Criptografia protege leitura, hash compara uma impressão sem reverter, encoding só representa dados em outro formato.

## Vocabulário

| Português | Inglês | Definição |
| --- | --- | --- |
| endereço IP | IP address | endereço de rede de uma interface |
| DNS | Domain Name System | resolução de nome para IP |
| porta / socket | port / socket | destino de serviço / endereço+porta+protocolo |
| timeout | timeout | prazo expirou sem resposta |
| firewall | firewall | regras que filtram tráfego |
| segredo | secret | credencial que não deve ser publicada |

## Demonstração guiada

1. Preveja: nome ou IP? Execute `nslookup example.com`; se ausente, Linux/macOS `dig example.com` ou PowerShell `Resolve-DnsName example.com`.
2. Execute `curl -I https://example.com`. Uma linha `HTTP/... 200` ou redirecionamento prova resposta HTTP, não que seu programa esteja correto.
3. Linux/WSL: `ss -ltn`; macOS: `lsof -nP -iTCP -sTCP:LISTEN`; PowerShell: `Get-NetTCPConnection -State Listen`. Veja portas locais sem testar sistemas externos.
4. Compare: DNS falha antes de conectar; “connection refused” chega ao host, mas não encontra listener; timeout não recebe resposta no prazo; HTTP 401/404/500 é resposta do servidor.
5. Crie `.env.example`, nunca `.env` versionado, com nomes sem valores reais: `DATABASE_URL=`, `REDIS_URL=`. Confira `git status` antes de adicionar arquivos.

## Exercício prático

**Objetivo:** escrever um mini relatório de uma requisição pública segura. **Ponto de partida:** `https://example.com`. **Segurança:** não faça scanner, força bruta nem teste portas de terceiros; não publique cabeçalhos com cookies. **Aceitação:** registre hostname consultado, resultado DNS, código HTTP e hipótese para uma falha hipotética. **Verificação:** rode `curl -I` novamente e compare apenas código e servidor. **Pistas graduais:** (1) use `--max-time 5` se a rede estiver lenta; (2) DNS pode resolver mesmo se HTTP falhar; (3) código HTTP só existe após resposta. Compare depois com o [spoiler comentado](../solutions/03-networking-and-security-solution.md).

## Desafio

O browser abre um site, mas `curl` diz “Could not resolve host”. Liste duas hipóteses e uma verificação para cada uma, sem mudar firewall ou DNS do sistema.

## Se algo deu errado

| Sintoma | Causa provável | Verificação |
| --- | --- | --- |
| nome não resolve | DNS, rede ou nome digitado errado | `nslookup` e confira grafia |
| connection refused | processo não escuta a porta | inspecione listener e configuração |
| timeout | rota, firewall ou serviço sem resposta | `curl --max-time 5`; tente endpoint conhecido |
| HTTP 401/403 | identidade válida ou permissão insuficiente | leia documentação; não tente credenciais aleatórias |

## Checkpoint

- [ ] Descrevo nome → DNS → conexão → TLS → HTTP → resposta.
- [ ] Diferencio quatro classes de falha por evidência.
- [ ] Sei que segredos ficam fora de Git e bancos locais não devem ser expostos à internet.

## Perguntas de reflexão

1. Qual evidência separa conexão recusada de credencial incorreta?
2. Por que encoding não protege um token, mas hashing pode ajudar a comparar senhas?

## Aprofundamento

Pesquise **“TCP connection refused versus timeout”**, **“TLS handshake overview”** e **“authentication authorization difference”**. Leia [documentação do GitHub sobre secrets](https://docs.github.com/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions) (complementar) para ver como CI recebe segredos sem gravá-los.

## Resumo

- DNS, TCP e HTTP são etapas diferentes e deixam evidências diferentes.
- Portas identificam serviços no host.
- Menor privilégio, segredos fora do Git e leitura de comandos reduzem risco.
