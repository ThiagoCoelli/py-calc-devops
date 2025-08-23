"""Interface de linha de comando (CLI) para a calculadora."""

from calculator.core import add, sub, mul, div


OPS = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


def _parse_number(prompt: str) -> float:
    """Lê um número do usuário. Aceita vírgula ou ponto como separador decimal."""
    raw = input(prompt).strip().replace(",", ".")
    return float(raw)


def run() -> None:
    print("=== Calculadora (CLI) ===")
    print("Digite dois números e escolha um operador (+, -, *, /).")
    print("Obs.: você pode usar vírgula ou ponto como separador decimal.\n")
    try:
        a = _parse_number("Primeiro número: ")
        op = input("Operador (+, -, *, /): ").strip()
        b = _parse_number("Segundo número: ")

        if op not in OPS:
            print("Operador inválido. Use apenas +, -, * ou /.")
            return

        resultado = OPS[op](a, b)
        # Usa formatação 'g' para mostrar inteiro sem .0 quando aplicável, mas manter precisão
        print(f"\nResultado: {resultado:g}")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números válidos.")
    except ZeroDivisionError as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    run()