"""Núcleo da calculadora: operações aritméticas básicas."""

from typing import Union

Number = Union[int, float]


__all__ = ["add", "sub", "mul", "div"]


def add(a: Number, b: Number) -> float:
    """Soma dois números.

    Args:
        a: Primeiro número.
        b: Segundo número.

    Returns:
        A soma (a + b) como float.
    """
    return float(a) + float(b)


def sub(a: Number, b: Number) -> float:
    """Subtrai dois números.

    Args:
        a: Minuendo.
        b: Subtraendo.

    Returns:
        A diferença (a - b) como float.
    """
    return float(a) - float(b)


def mul(a: Number, b: Number) -> float:
    """Multiplica dois números.

    Args:
        a: Primeiro fator.
        b: Segundo fator.

    Returns:
        O produto (a * b) como float.
    """
    return float(a) * float(b)


def div(a: Number, b: Number) -> float:
    """Divide dois números.

    Args:
        a: Dividendo.
        b: Divisor.

    Returns:
        O quociente (a / b) como float.

    Raises:
        ZeroDivisionError: Se b == 0.
    """
    b = float(b)
    if b == 0.0:
        raise ZeroDivisionError("Divisão por zero não é permitida.")
    return float(a) / b