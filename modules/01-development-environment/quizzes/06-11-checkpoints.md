# Checkpoints das Unidades 6–11

Responda antes de abrir o [gabarito comentado](06-11-checkpoints-answers.md). Explique evidências quando a pergunta pedir decisão.

1. **Múltipla escolha.** No VS Code, qual ação dá evidência mais direta de que o projeto usará as dependências declaradas? (A) trocar o tema; (B) selecionar `.venv` criado por `uv sync`; (C) instalar muitas extensões; (D) abrir uma janela sem pasta.
2. **Interpretação de saída.** Um debugger para em `AttributeError: 'str' object has no attribute 'lowercase'` na linha `name.strip().lowercase()`. Qual é a correção mais provável? Que observação da stack trace confirma onde investigar?
3. **Múltipla escolha.** Qual afirmação é correta? (A) `git add` publica no GitHub; (B) `git commit` cria um remoto; (C) staging escolhe o conteúdo do próximo commit; (D) PR substitui commits locais.
4. **Resposta aberta.** Um conflito tem `cache_ttl_seconds=120` de uma branch e comentário explicativo de outra. Como você decide e quais passos usam Git para finalizar sem reescrever histórico?
5. **Múltipla escolha.** Qual arquivo registra a resolução concreta de dependências Python neste projeto? (A) `README.md`; (B) `pyproject.toml`; (C) `uv.lock`; (D) `__init__.py`.
6. **Interpretação de saída.** `uv run pytest` passa, mas `uv run ruff format --check .` falha em um arquivo. O que isso informa sobre o comportamento do programa e qual ação segura vem depois?
7. **Múltipla escolha.** Uma interface TypeScript garante que JSON recebido de uma API tenha os campos corretos em runtime? (A) sempre; (B) somente se o JSON vier de Node; (C) não, é preciso validar dados em runtime; (D) somente com ESM.
8. **Resposta aberta.** A CI falha no step `npm run typecheck`, enquanto testes Python passam localmente. Quais três evidências você coleta antes de alterar código?
9. **Múltipla escolha.** PostgreSQL está saudável e Redis foi parado no desafio. Qual resposta respeita o desenho do laboratório? (A) apagar o volume PostgreSQL; (B) tratar Redis como fonte de verdade; (C) registrar cache indisponível, restaurar Redis e preservar PostgreSQL; (D) abrir a porta do Redis à internet.
10. **Resposta aberta.** Liste as evidências mínimas que seu PR final deve conter para alguém reproduzir a melhoria sem receber seu `.env`.
