# Spoiler — Unidade 9

## Resposta trabalhada

Um teste adicional pode seguir o formato existente:

```ts
it('normalizes spaces and mixed-case species', () => {
  expect(validatePatient(' Mimo ', ' CAT ', 2020, 2026)).toEqual({
    name: 'Mimo', species: 'cat', birth_year: 2020,
  });
});
```

Depois, execute `npm run test`, `npm run lint`, `npm run format` e `npm run typecheck`. Para o desafio, `return ALLOWED_SPECIES.has(value.trim().toLowerCase())` cobre a consulta. Ela não substitui `validatePatient`: apenas responde sobre espécie e não protege nome, ano nem formato completo do objeto.
