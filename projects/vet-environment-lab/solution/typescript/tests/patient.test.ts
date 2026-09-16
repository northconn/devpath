import { describe, expect, it } from 'vitest';

import {
  patientSummary,
  ValidationError,
  validatePatient,
} from '../src/index.js';

describe('validatePatient', () => {
  it('normalizes valid synthetic input', () => {
    const patient = validatePatient('  Luna  ', 'DOG', 2021, 2026);

    expect(patient).toEqual({ name: 'Luna', species: 'dog', birth_year: 2021 });
    expect(patientSummary(patient)).toEqual(patient);
  });

  it.each([
    [' ', 'dog', 2021, 'name'],
    ['Luna', 'iguana', 2021, 'species'],
    ['Luna', 'dog', 2027, 'birth_year'],
  ])('rejects invalid input: %s', (name, species, birthYear, message) => {
    expect(() => validatePatient(name, species, birthYear, 2026)).toThrow(
      new RegExp(message),
    );
    expect(() => validatePatient(name, species, birthYear, 2026)).toThrow(
      ValidationError,
    );
  });

  it.each([Number.NaN, 2021.5])(
    'rejects a non-integer birth year: %s',
    (birthYear) => {
      expect(() => validatePatient('Luna', 'dog', birthYear, 2026)).toThrow(
        /birth_year/,
      );
    },
  );
});
