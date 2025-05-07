inicio = int(input("Digite o valor inicial em Fahrenheit: "))
final = int(input("Digite o valor final em Fahrenheit: "))

print("\nFahrenheit | Celsius")
print("---------------------")

if inicio <= final:
    for f in range(inicio, final + 1):
        c = 5 * (f - 32) / 9
        print(f"{f:10d} °F | {c:6.3f} °C")
else:
    for f in range(inicio, final - 1, -1):
        c = 5 * (f - 32) / 9
        print(f"{f:10d} °F | {c:6.3f} °C")