import math

def calcular_volume_esfera(raio: float) -> float:
    return (4 / 3) * math.pi * raio ** 3

def calcular_necessidade_agua(peso: float) -> float:
    return peso * 0.03

def calcular_distancia_pontos(x1, y1, x2, y2) -> float:
    return math.hypot(x2 - x1, y2 - y1)

def ordenar_valores(a: int, b: int) -> tuple:
    return tuple(sorted([a, b]))

def calcular_peso_ideal(altura: float, sexo: str) -> float:
    sexo = sexo.upper()
    if sexo == 'M':
        return (72.7 * altura) - 58
    elif sexo == 'F':
        return (62.1 * altura) - 44.7
    else:
        raise ValueError("Sexo inválido")

def menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Calcular volume de uma esfera")
        print("2 - Calcular necessidade diária de água")
        print("3 - Calcular distância entre dois pontos")
        print("4 - Ordenar dois valores inteiros")
        print("5 - Calcular peso ideal")
        print("0 - Sair")

        try:
            opcao = int(input("Escolha uma opção (0-5): "))
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
            continue

        if opcao == 0:
            print("Saindo do programa.")
            break
        elif opcao == 1:
            try:
                r = float(input("Digite o raio da esfera: "))
                v = calcular_volume_esfera(r)
                print(f"O volume da esfera é: {v:.2f}")
            except ValueError:
                print("Valor inválido para o raio.")
        elif opcao == 2:
            try:
                peso = float(input("Digite seu peso em kg: "))
                necessidade = calcular_necessidade_agua(peso)
                print(f"Sua necessidade diária de água é: {necessidade:.2f} litros")
            except ValueError:
                print("Valor inválido para o peso.")
        elif opcao == 3:
            try:
                x1 = float(input("Digite x1: "))
                y1 = float(input("Digite y1: "))
                x2 = float(input("Digite x2: "))
                y2 = float(input("Digite y2: "))
                d = calcular_distancia_pontos(x1, y1, x2, y2)
                print(f"A distância entre os pontos é: {d:.2f}")
            except ValueError:
                print("Coordenadas inválidas.")
        elif opcao == 4:
            try:
                a = int(input("Digite o primeiro valor inteiro: "))
                b = int(input("Digite o segundo valor inteiro: "))
                menor, maior = ordenar_valores(a, b)
                print(f"Valores em ordem crescente: {menor}, {maior}")
            except ValueError:
                print("Digite apenas valores inteiros.")
        elif opcao == 5:
            try:
                altura = float(input("Digite sua altura em metros: "))
                sexo = input("Digite seu sexo (M para masculino, F para feminino): ")
                peso_ideal = calcular_peso_ideal(altura, sexo)
                print(f"Seu peso ideal é: {peso_ideal:.2f} kg")
            except ValueError as e:
                print(e)
        else:
            print("Opção inválida!")

# Executa o menu
if __name__ == "__main__":
    menu()
