# Spoiler — Unidade 2

## Resposta trabalhada

Em Linux/macOS, uma solução deliberadamente limitada à pasta temporária é:

```bash
mkdir -p /tmp/devpath-files/{draft,review,published}
printf 'synthetic\n' > /tmp/devpath-files/draft/item.txt
mv /tmp/devpath-files/draft/item.txt /tmp/devpath-files/published/item.txt
ls /tmp/devpath-files/draft
rg synthetic /tmp/devpath-files/published
```

`ls draft` não deve mostrar `item.txt`; `rg` deve imprimir a linha com `synthetic`. Em PowerShell, `New-Item -ItemType Directory -Force`, `Set-Content`, `Move-Item`, `Get-ChildItem` e `Select-String` fazem os papéis correspondentes usando `$env:TEMP\devpath-files`. `cp` não é o comando PowerShell padrão: `Copy-Item` é, e `Get-Help Copy-Item -Examples` mostra a sintaxe. Caminhos explícitos tornam a remoção posterior revisável.
