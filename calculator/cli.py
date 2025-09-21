"""Interface de linha de comando (CLI) para a calculadora."""

from calculator.core import add, sub, mul, div
from typing import Callable, Dict

OPS: Dict[str, Callable[[float, float], float]] = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


def _parse_number(prompt: str) -> float:
    """Lê um número do usuário. Aceita vírgula ou ponto como separador decimal."""
    raw = input(prompt).strip().replace(",", ".")
    return float(raw)


def calcular(a: float, op: str, b: float) -> float:
    """
    Executa a operação entre a e b usando o operador op.
    Lança ValueError se o operador for inválido. Pode propagar ZeroDivisionError.
    """
    if op not in OPS:
        raise ValueError(f"Operador inválido: {op}")
    return OPS[op](a, b)


def run() -> None:
    """Loop único de interação com o usuário (uma operação)."""
    print("=== Calculadora (CLI) ===")
    print("Digite dois números e escolha um operador (+, -, *, /).")
    print("Obs.: você pode usar vírgula ou ponto como separador decimal.\n")
    try:
        a = _parse_number("Primeiro número: ")
        op = input("Operador (+, -, *, /): ").strip()
        b = _parse_number("Segundo número: ")

        resultado = calcular(a, op, b)
        # Usa formatação 'g' para mostrar inteiro sem .0 quando aplicável, mas manter precisão
        print(f"\nResultado: {resultado:g}")

    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números válidos ou um operador correto.")
    except ZeroDivisionError as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    run()
