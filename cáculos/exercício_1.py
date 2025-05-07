import math

def calcular_volume_esfera():
    r = float(input("Digite o raio da esfera: "))
    volume = (4/3) * math.pi * (r ** 3)
    print(f"O volume da esfera é: volume:.2f")

def calcular_necessidade_agua():
    massa = float(input("Digite seu peso em kg: "))
    necessidade = massa * 0.03
    print(f"Sua necessidade diária de água é: necessidade:.2f litros")

def calcular_distancia_pontos():
    x1 = float(input("Digite x1: "))
    y1 = float(input("Digite y1: "))
    x2 = float(input("Digite x2: "))
    y2 = float(input("Digite y2: "))
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(f"A distância entre os pontos é: distancia:.2f")

def ordenar_valores():
    a = int(input("Digite o primeiro valor inteiro: "))
    b = int(input("Digite o segundo valor inteiro: "))
    if a > b:
        a, b = b, a  # Troca os valores se estiverem na ordem errada
    print(f"Valores em ordem crescente: a, b")

def calcular_peso_ideal():
    altura = float(input("Digite sua altura em metros: "))
    sexo = input("Digite seu sexo (M para masculino, F para feminino): ").strip().upper()
    if sexo == 'M':
        peso_ideal = (72.7 * altura) - 58
    elif sexo == 'F':
        peso_ideal = (62.1 * altura) - 44.7
    else:
        print("Sexo inválido!")
        return
    print(f"Seu peso ideal é: {peso_ideal:.2f} kg")

print("1 - Calcular volume de uma esfera")
print("2 - Calcular necessidade diária de água")
print("3 - Calcular distância entre dois pontos")
print("4 - Ordenar dois valores inteiros")
print("5 - Calcular peso ideal")
opcao = int(input("Escolha uma opção (1-5): "))

if opcao == 1:
    calcular_volume_esfera()
elif opcao == 2:
    calcular_necessidade_agua()
elif opcao == 3:
    calcular_distancia_pontos()
elif opcao == 4:
    ordenar_valores()
elif opcao == 5:
    calcular_peso_ideal()
else:
    print("Opção inválida!")