# Solução de referência

Esta solução prioriza funções pequenas e nomes explícitos. O PostgreSQL é a fonte de verdade; o Redis guarda somente um resumo temporário por 300 segundos.

As consultas em `python/src/vet_environment_lab/database.py` usam parâmetros separados da string SQL. Nunca concatene entrada de pessoas em SQL: isso evita injeção de SQL.
