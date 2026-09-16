/** Dados sintéticos de um paciente do laboratório, sem qualquer regra clínica. */
export interface PatientInput {
  name: string;
  species: string;
  birth_year: number;
}

export const ALLOWED_SPECIES = new Set(['bird', 'cat', 'dog', 'rabbit']);

export class ValidationError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'ValidationError';
  }
}

/** Normaliza e valida nome, espécie e ano de nascimento fictícios. */
export function validatePatient(
  name: string,
  species: string,
  birthYear: number,
  currentYear = new Date().getFullYear(),
): PatientInput {
  const normalizedName = name.trim();
  const normalizedSpecies = species.trim().toLowerCase();

  if (normalizedName.length < 2 || normalizedName.length > 80) {
    throw new ValidationError('name must contain between 2 and 80 characters');
  }
  if (!ALLOWED_SPECIES.has(normalizedSpecies)) {
    throw new ValidationError(
      `species must be one of: ${[...ALLOWED_SPECIES].sort().join(', ')}`,
    );
  }
  if (
    !Number.isInteger(birthYear) ||
    birthYear < 1900 ||
    birthYear > currentYear
  ) {
    throw new ValidationError(
      `birth_year must be between 1900 and ${currentYear}`,
    );
  }

  return {
    name: normalizedName,
    species: normalizedSpecies,
    birth_year: birthYear,
  };
}

/** Retorna o mesmo formato simples usado para mostrar um paciente validado. */
export function patientSummary(patient: PatientInput): PatientInput {
  return { ...patient };
}
