from models.function import calcular

while True:

# Solicitando ao usuário que insira os valores e a operação desejada
    x = input('''
Escolha a operação que você gostaria de realizar: 

+ para adição
- para subtração
* para multiplicação
/ para divisão

''')

    a = int(input("Digite aqui o primeiro número: "))
    b = int(input("Digite aqui o segundo número: "))

# Chamando a função calcular para executar a lógica
    calcular(x, a, b)

    resposta = input('Quer calcular novamente? Digite S para sim e N para não: ')
    if resposta.upper() != 'S':
        print('Te vejo mais tarde')
        break  # Sai do loop se a resposta não for 'S'


