"""Comando inicial: uma pequena evidência de que o ambiente funciona."""

import platform
import sys


def main() -> None:
    """Mostra somente informações que podem ser compartilhadas com segurança."""
    print("Olá, Vet Environment Lab!")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Sistema: {platform.system()} {platform.release()}")
    print("Próximo passo: implemente a validação de um paciente fictício.")


if __name__ == "__main__":
    main()
