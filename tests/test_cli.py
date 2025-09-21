from calculator.cli import calcular
import builtins
import pytest
from io import StringIO
import sys

def test_calcular_ops():
    assert calcular(2, "+", 3) == 5.0
    assert calcular(5, "-", 2) == 3.0
    assert calcular(3, "*", 4) == 12.0
    assert calcular(7, "/", 2) == 3.5

def test_calcular_invalid_op():
    with pytest.raises(ValueError):
        calcular(1, "%", 2)

def run_cli_with_inputs(monkeypatch, inputs):
    """
    Helper: executa run() substituindo input() por valores do iter(inputs)
    e captura o stdout retornando a saída como string.
    """
    import calculator.cli as cli

    it = iter(inputs)
    monkeypatch.setattr(builtins, "input", lambda prompt="": next(it))
    captured = StringIO()
    old = sys.stdout
    try:
        sys.stdout = captured
        cli.run()
    finally:
        sys.stdout = old
    return captured.getvalue()

def test_run_cli_success(monkeypatch):
    out = run_cli_with_inputs(monkeypatch, ["2", "+", "3"])
    assert "Resultado" in out
    assert "5" in out  # resultado 5

def test_run_cli_invalid_number(monkeypatch):
    out = run_cli_with_inputs(monkeypatch, ["abc", "+", "1"])
    assert "Entrada inválida" in out

def test_run_cli_division_by_zero(monkeypatch):
    out = run_cli_with_inputs(monkeypatch, ["5", "/", "0"])
    assert "Divisão por zero" in out or "Erro:" in out
