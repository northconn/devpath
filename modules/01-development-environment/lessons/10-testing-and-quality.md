# Unidade 10 — Testes, qualidade e integração contínua

## Resultado esperado

Você escreverá um teste que falha antes da correção, distinguirá teste, lint, formatação e checagem de tipos, e investigará uma falha local ou de CI por evidências.

## Tempo estimado

150–210 minutos.

## Pré-requisitos

Unidades 7–9; ambientes Python e TypeScript sincronizados. PostgreSQL e Redis não são necessários para os testes unitários de validação.

## Por que isso importa

“Funcionou uma vez” mostra apenas uma execução. Um teste que reproduz um defeito impede que ele volte quando o código mudar. CI executa as mesmas verificações em ambiente limpo, reduzindo a diferença entre máquina local e revisão.

## Modelo mental

Teste unitário verifica uma unidade pequena e isolada, como `validate_patient`; teste de integração verifica cooperação entre componentes, como aplicação e PostgreSQL; ponta a ponta verifica um fluxo completo. Aqui o foco é unidade. **Arrange–Act–Assert** significa preparar dados, agir chamando a função e verificar saída ou erro.

Lint encontra padrões suspeitos; formatter torna estilo consistente; type checker compara o programa às anotações de tipo; teste executa comportamento. Eles se complementam. Depurar segue um ciclo: reproduzir, reduzir ao menor caso, formular hipótese, observar evidência, mudar o mínimo e executar a verificação que falhava.

No GitHub Actions, um **evento** como push ou PR inicia um **workflow**; ele possui **jobs**, cada job roda em um **runner**, e cada job possui **steps**. O workflow raiz em `.github/workflows/ci.yml` e o template em `.github/pull_request_template.md` fazem parte do fluxo deste curso. A CI deve executar os checks da referência e também os testes e verificações que você acrescentar em `starter/python`; um PR só está pronto para revisão quando os jobs obrigatórios estão verdes.

## Vocabulário

| Português | Inglês | Definição |
| --- | --- | --- |
| teste unitário | unit test | verifica função pequena em isolamento |
| preparar–agir–verificar | Arrange–Act–Assert | estrutura legível de teste |
| lint | lint | análise de padrões e erros prováveis |
| formatação | formatting | estilo automático e previsível |
| checagem de tipos | type checking | coerência com tipos declarados |
| integração contínua | continuous integration / CI | verificações automatizadas de mudanças |

## Demonstração guiada

1. No Python, entre em `projects/vet-environment-lab/solution/python` e execute:

   ```bash
   uv sync --all-groups
   uv run pytest
   uv run ruff check .
   uv run ruff format --check .
   ```

   Os testes de `tests/test_validation.py` não abrem banco: isso é uma propriedade de teste unitário, não falta de cobertura.
2. Leia o caso de espécie `iguana`. Arrange prepara os valores; Act chama `validate_patient`; Assert espera `ValidationError` cuja mensagem inclui `species`. Antes de mudar produção, acrescente numa cópia o teste para `' DOG '` e preveja que ele passará pela normalização.
3. Pratique vermelho–verde: troque temporariamente, numa cópia de trabalho, `normalized_species = species.strip().lower()` por `normalized_species = species.strip()`. Rode `uv run pytest`: o teste de caixa alta falha. A hipótese é que falta normalização de caixa. Restaure `lower()`, rode novamente e obtenha verde. O teste existia antes da correção, portanto demonstra a regressão.
4. Para uma falha de formato segura, em sua cópia acrescente uma linha com espaços no fim de um arquivo Python. Rode `uv run ruff format --check .`; leia o arquivo indicado. Use `uv run ruff format .`, revise `git diff` e rode o check novamente. Não aplique formatador em arquivos que você não revisou.
5. No TypeScript, entre em `../typescript` e execute `npm ci`, `npm run test`, `npm run lint`, `npm run format` e `npm run typecheck`. `tsc --noEmit` verifica tipos sem gerar artefatos. Veja que Vitest testa comportamento e ESLint/Prettier não são substitutos um do outro.
6. Abra `.github/workflows/ci.yml` e localize os jobs Python e TypeScript. Quando seu desafio criar testes em `projects/vet-environment-lab/starter/python`, garanta que o job Python também entra nesse diretório, sincroniza as dependências declaradas no starter e executa `uv run pytest`, `uv run ruff check .` e `uv run ruff format --check .`. A versão do runtime, comandos e lockfiles devem coincidir com `docs/tooling-versions.md`; não copie YAML de fonte desconhecida. No PR, abra a execução, identifique job/step falho e compare o comando exibido com a reprodução local.

## Exercício prático

**Objetivo:** impedir a volta de um erro de normalização de espécie. **Ponto de partida:** cópia de `solution/python` com ambiente sincronizado. **Segurança:** modifique somente dados e arquivos do exercício; não desative verificações nem altere lockfiles sem dependência nova. **Aceitação:** há teste explícito para espaços e caixa mista; ele falha quando `lower()` é removido e passa quando é restaurado; pytest e os dois checks Ruff passam. **Verificação:** registre saída dos três comandos e o diff do teste. **Pistas graduais:** (1) use `test_validate_patient_normalizes_valid_synthetic_input` como modelo; (2) mude uma causa por vez; (3) uma falha de formatter informa arquivo e regra, não uma falha funcional. Veja o [spoiler comentado](../solutions/10-testing-and-quality-solution.md) depois de tentar.

## Desafio

Uma CI hipotética mostra `npm run typecheck` falhando em `src/patient.ts` por atribuir `birth_year: '2021'` a `PatientInput`. Sem alterar o tipo para `any`, formule hipótese, reproduza localmente em uma cópia e corrija o valor para número. Explique por que essa CI pode falhar embora o teste Python esteja verde.

## Se algo deu errado

| Sintoma | Causa provável | Verificação |
| --- | --- | --- |
| teste falha após mudança | comportamento ou expectativa mudou | leia expected/actual e reduza a entrada |
| Ruff aponta arquivo inesperado | formatter detectou estilo no arquivo | abra só o arquivo citado, rode format e revise diff |
| `npm ci` falha na CI | lockfile não corresponde ao manifesto | confira mudanças em `package.json` e `package-lock.json` |
| CI falha, local passa | runtime, lockfile, SO ou comando diferentes | compare versão e step exato no log |
| teste exige Docker sem necessidade | regra misturada com infraestrutura | extraia função pura e mantenha integração em teste separado |

## Checkpoint

- [ ] Executei as verificações Python e TypeScript do repositório.
- [ ] Produzi um teste vermelho e o tornei verde com mudança mínima.
- [ ] Sei localizar evento, job e step em um log de GitHub Actions.

## Perguntas de reflexão

1. Que regressão um teste unitário de validação detecta que lint não detecta?
2. O que comparar primeiro quando CI falha mas sua máquina passa?
3. Por que mudar expectativa de teste para “fazer verde” pode esconder um bug?

## Aprofundamento

Pesquise **“pytest parametrization raises”**, **“Ruff check versus format”** e **“GitHub Actions workflow job step runner”**. Leia [pytest: getting started](https://docs.pytest.org/en/stable/getting-started.html) (essencial), [Ruff](https://docs.astral.sh/ruff/) (essencial), [Vitest guide](https://vitest.dev/guide/) (complementar) e [GitHub Actions docs](https://docs.github.com/actions) (essencial).

## Resumo

- Teste prova comportamento específico; lint, formato e tipos observam outras classes de problema.
- Vermelho–verde liga correção a uma regressão reproduzível.
- CI deve executar comandos declarados e ambientes reproduzíveis.
- Um log de CI é evidência: encontre o step, reproduza o comando e só então corrija.
