from calculator.core import add, sub, mul, div

OPS= {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}

def run():
    print("=== Calculadora (CLI) ===")
    print("Operações: + - * /")
    try:
        a = float(input("Digite o primeiro número: "))
        op = input("Operador: ").strip()
        b = float(input("Digite o segundo: "))
        if op not in OPS:
            print("Operador inválido")
            return
        print(f"Resultado: {OPS[op](a, b)}")
    except ValueError:
        print("Entrada invalida. Use números.")
    except ZeroDivisionError: as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    run()