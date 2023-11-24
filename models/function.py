#função que tem outras funções dentro para definir operações, aceita argumentos x = operador, e ab números
def calcular(x, a, b):
    try:
        a = float(a)  # Tenta converter 'a' para float
        b = float(b)  # Tenta converter 'b' para float
    except ValueError:
        print("Erro: Insira apenas números.")
        return
    def soma(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mult(a, b):
        return a * b

    def div(a, b):
        if b == 0:
            print('Você não pode dividir por zeros')
            return
        return a / b

    if x == '+':
        print(f'A soma de {a} e {b} =', soma(a, b))
    elif x == '-':
        print(f'A subtração de {a} e {b} =', sub(a, b))
    elif x == '/':
        print(f'A divisão de {a} por {b} =', div(a, b))
    elif x == '*':
        print(f'A multiplicação de {a} por {b} =', mult(a, b))
    else:
        print("Você não digitou um operador válido")