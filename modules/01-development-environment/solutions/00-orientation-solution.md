# Spoiler — Unidade 0

## Resposta trabalhada

Partindo de `projects/vet-environment-lab/starter/python`, executei:

```bash
uv run vet-environment-lab hello
cd ../../../..
pwd
ls PROGRESS.md
```

O último `ls` deve imprimir `PROGRESS.md`; isso é a evidência de que quatro `..` voltaram de `python` para a raiz. Uma evidência adequada é: “16/09/2026, Ubuntu no WSL: executei `hello`; a saída confirmou versão de Python e sistema, sem identificar minha conta.” Ela prova contexto e resultado sem copiar caminho pessoal ou variáveis.

`cd` pede ao shell que troque o diretório atual; por isso `pwd` muda. Terminal é a janela, shell interpreta `cd`, e o programa `hello` é outro processo chamado pelo shell.
