# Referência em TypeScript

Esta é uma comparação curta com a validação Python do Vet Environment Lab. Usa somente pacientes fictícios e não contém lógica clínica.

## Executar

Requer Node.js 24 LTS e npm. A versão é fixada pelo `package-lock.json`:

```bash
npm ci
npm run test
npm run lint
npm run format
npm run typecheck
```

## Comparar arquivo por arquivo

| Python                                            | TypeScript                       | Papel                                                                                      |
| ------------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------ |
| `../python/src/vet_environment_lab/validation.py` | `src/patient.ts`                 | Espécies permitidas, erro e normalização/validação.                                        |
| `../python/src/vet_environment_lab/models.py`     | `src/patient.ts`                 | Formato `name`, `species` e `birth_year`; `patientSummary` devolve uma cópia desse resumo. |
| `../python/tests/test_validation.py`              | `tests/patient.test.ts`          | Entradas válidas, inválidas e mensagens de erro.                                           |
| `../python/pyproject.toml`                        | `package.json` e `tsconfig.json` | Dependências, scripts e checagem de tipos.                                                 |

`PatientInput` é uma interface TypeScript, usada apenas na checagem de tipos. `validatePatient` produz o mesmo formato normalizado da função Python `validate_patient`; o parâmetro opcional `currentYear` deixa o teste de ano futuro determinístico.
