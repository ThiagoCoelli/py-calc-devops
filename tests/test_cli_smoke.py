def test_cli_import():
    # Teste de fumaça: garante que o módulo CLI importa sem explodir dependências
    import importlib
    m = importlib.import_module("calculator.cli")
    assert hasattr(m, "run")