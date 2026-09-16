# Spoiler — Unidade 11

## Resposta trabalhada

Uma solução mínima cria uma função pura de validação e resumo, um subcomando `summary` no ponto de entrada e testes para uma entrada válida, espécie inválida e ano futuro. A saída válida para `--name "  Luna  " --species DOG --birth-year 2021` é JSON com `Luna`, `dog` e `2021`.

O caminho de referência para comparar responsabilidades está em `../../../projects/vet-environment-lab/solution/python/`: `validation.py` contém regras, `models.py` representa dados, `cli.py` traduz argumentos e `tests/test_validation.py` protege comportamento. Compare os arquivos depois de construir sua versão; não copie o diretório inteiro.

Uma retrospectiva aceitável registra: “Escolhi testar a validação sem Docker porque a função não depende de rede. Parei Redis com `docker compose --env-file .env stop redis`, confirmei que o starter mostrou PostgreSQL `running` e Redis parado em `ps`, iniciei-o novamente e não removi volume. Também incluí `starter/python` no job Python da CI, que executou pytest e Ruff com resultado verde. Próximo passo: acrescentar teste de integração separado para persistência.” A rubrica avalia essa explicação junto com comandos e resultados.
