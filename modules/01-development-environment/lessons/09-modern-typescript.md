# Unidade 9 — JavaScript e TypeScript modernos

## Resultado esperado

Você executará a referência TypeScript, seguirá imports ESM e explicará por que uma interface ajuda no desenvolvimento, mas não torna entrada externa válida em runtime.

## Tempo estimado

100–145 minutos.

## Pré-requisitos

Unidade 8 e Node.js LTS com npm. O projeto declara Node 24 LTS; confirme a instalação com `node --version` e `npm --version`.

## Por que isso importa

Ao abrir um repositório, `package.json`, `package-lock.json`, `src/`, `tests/` e scripts indicam rapidamente como instalar, testar e verificar a aplicação. Reconhecer essa estrutura evita executar comandos aleatórios ou misturar ferramentas de outro ecossistema.

## Modelo mental

JavaScript executa em runtimes como navegadores e Node.js. Node executa o código deste laboratório no terminal. TypeScript acrescenta sintaxe de tipos e o compilador verifica coerência antes da execução; o JavaScript gerado não valida automaticamente aquilo que chegou por rede, arquivo ou formulário. Portanto `PatientInput` documenta o formato esperado, enquanto `validatePatient` ainda verifica texto, espécie e ano em runtime.

Este projeto usa **ESM** (ECMAScript Modules): `export` torna algo disponível e `import` o consome. `"type": "module"` em `package.json` seleciona esse formato; imports locais de TypeScript usam sufixo `.js` porque o código emitido para Node o terá. `package-lock.json` fixa a árvore resolvida e `npm ci` instala exatamente essa árvore, adequado para CI.

## Vocabulário

| Português | Inglês | Definição |
| --- | --- | --- |
| runtime | runtime | programa que executa JavaScript |
| tipo | type | descrição de valores aceitos pelo compilador |
| transpilar | transpile | transformar TypeScript em JavaScript |
| módulo ESM | ECMAScript Module | arquivo que usa `import` e `export` padrão |
| dependência de desenvolvimento | dev dependency | ferramenta necessária para desenvolver, não para executar o produto |
| verificação em runtime | runtime validation | checagem enquanto o programa está em execução |

## Demonstração guiada

1. Entre em `projects/vet-environment-lab/solution/typescript`, leia `package.json` e execute:

   ```bash
   node --version
   npm --version
   npm ci
   npm run test
   npm run lint
   npm run format
   npm run typecheck
   ```

   `npm ci` usa o lockfile e pode remover `node_modules` local para torná-lo igual ao lockfile; não use-o com alterações não salvas dentro dessa pasta. Os scripts revelam Vitest, ESLint, Prettier e `tsc --noEmit`.
2. Abra `src/index.ts`. Ele reexporta nomes de `patient.ts`. Siga `validatePatient`: `PatientInput` exige `name`, `species` e `birth_year`; `ValidationError` comunica entrada inválida; a função remove espaços, coloca espécie em minúsculas e compara o ano.
3. Antes de executar testes, preveja o resultado de `validatePatient('  Luna  ', 'DOG', 2021, 2026)`: um objeto com `Luna`, `dog` e `2021`. Em `tests/patient.test.ts`, o quarto argumento fixa `2026`, deixando o teste repetível mesmo em outro ano.
4. Veja o limite de tipos: em uma cópia de experimento, `const input: PatientInput = { name: 'Luna', species: 'dog', birth_year: 2021 };` é conferido pelo TypeScript. Porém JSON vindo de fora pode conter `birth_year: "2021"`; a interface desaparece no JavaScript executado. Chamar `validatePatient` é o que rejeita `NaN`, decimal, espécie inválida e ano futuro.
5. Compare com Python: ambos normalizam e lançam erro de validação. Python usa `dataclass` no modelo; TypeScript usa `interface` e objeto. Nenhuma escolha elimina validação de dados externos.

## Exercício prático

**Objetivo:** adicionar teste para uma espécie com espaços e caixa mista. **Ponto de partida:** `solution/typescript` instalado com `npm ci`, ou sua cópia da referência. **Segurança:** use somente pacientes fictícios; não edite `package-lock.json` manualmente e não instale pacote global para contornar falha local. **Aceitação:** o novo teste espera `{ name: 'Mimo', species: 'cat', birth_year: 2020 }` para `' Mimo '`, `' CAT '`, `2020`; os scripts `test`, `lint`, `format` e `typecheck` passam. **Verificação:** execute os quatro scripts de `package.json`. **Pistas graduais:** (1) copie a estrutura do primeiro teste e mude apenas os dados; (2) a expectativa deve refletir `trim()` e `toLowerCase()`; (3) formate com a ferramenta, não à mão. Veja o [spoiler comentado](../solutions/09-modern-typescript-solution.md) depois de tentar.

## Desafio

Crie uma função `isAllowedSpecies(value: string): boolean` em sua cópia que normalize somente espaços e caixa antes de consultar `ALLOWED_SPECIES`. Escreva testes para `' DOG '`, `'iguana'` e a string vazia. Depois, explique por que essa função de conveniência não substitui `validatePatient`, que também valida nome e ano.

## Se algo deu errado

| Sintoma | Causa provável | Verificação |
| --- | --- | --- |
| `node: command not found` | Node não está instalado ou no PATH | instale LTS e abra novo terminal; rode `node --version` |
| `npm ci` recusa lockfile | `package.json` e lockfile divergiram | restaure a coerência via dependência declarada e revisão de diff |
| erro de import ESM | extensão ou formato de módulo incoerente | confira `type: module`, `tsconfig.json` e imports `.js` locais |
| typecheck passa, execução falha | tipo não validou entrada externa | adicione validação em runtime e teste o valor real |
| Prettier falha | formatação diferente da regra do projeto | execute a correção orientada pelo README antes de commit |

## Checkpoint

- [ ] Executei `npm ci` e os quatro scripts do projeto.
- [ ] Localizei `type: module`, `exports` e imports ESM.
- [ ] Expliquei uma verificação do compilador e uma validação em runtime.

## Perguntas de reflexão

1. O que o lockfile oferece que só `package.json` não oferece?
2. Que entrada externa pode passar por uma interface no código, mas ainda ser inválida em runtime?
3. Como os testes determinísticos de ano evitam falha no futuro?

## Aprofundamento

Pesquise **“Node.js ECMAScript modules type module”**, **“TypeScript types erased runtime validation”** e **“npm ci lockfile CI”**. Leia [Node.js: introdução](https://nodejs.org/en/learn/getting-started/introduction-to-nodejs) (essencial), [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) (essencial) e [npm ci](https://docs.npmjs.com/cli/commands/npm-ci/) (complementar).

## Resumo

- Node é o runtime terminal desta referência; TypeScript é verificado antes de executar.
- ESM torna fronteiras entre módulos explícitas com `import` e `export`.
- Interface melhora coerência do código, mas entrada externa exige validação em runtime.
- `npm ci` usa o lockfile para uma instalação reproduzível.
