# Spoiler — Unidade 1

## Resposta trabalhada

Escolhi `uv` e executei:

```bash
command -v uv
uv --version
```

Se a primeira linha for, por exemplo, `/home/alguem/.local/bin/uv`, ela é a evidência de que o shell encontrou o executável por meio de `PATH`; a segunda confirma que ele inicia. Se vier vazia, a resposta correta é registrar “não encontrado no PATH” e consultar a instalação oficial, sem editar arquivos de perfil ou usar `sudo` por tentativa.

RAM insuficiente tende a aparecer em `free -h`/`vm_stat`, lentidão e processos encerrados; disco cheio aparece em espaço livre e erro ao gravar. São recursos diferentes. Remover arquivo muda armazenamento persistente; encerrar um processo encerra trabalho em RAM e pode perder dados ainda não gravados. Por isso a observação vem antes de qualquer ação.
