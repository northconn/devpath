# Spoiler — Unidade 7

## Resposta trabalhada

No laboratório temporário, após o `git merge docs-explanation`, `settings.txt` contém os marcadores de conflito. A resolução escolhida foi:

```text
cache_ttl_seconds=120 # temporary cache
```

Em seguida executei `git add settings.txt` e `git commit -m "merge: resolve cache setting conflict"`. Mantive 120 porque a branch de funcionalidade alterou o comportamento e preservei o comentário da branch documental. Outra escolha pode ser válida se a equipe justificar e testar.

No repositório publicado, a sequência segura é criar issue, `git switch -c docs/git-lab-note`, editar uma nota sem segredos, revisar `git diff`, selecionar só o arquivo com `git add`, revisar `git diff --staged`, fazer commit e abrir PR. Autoria vem de `user.name` e `user.email`; login no remoto vem de HTTPS com gerenciador de credenciais ou SSH.
