id = int(input("\nDigite sua matricula: "))

nota1 = float(input("Digite a 1° nota: "))
nota2 = float(input("Digite a 2° nota: "))
nota3 = float(input("Digite a 3° nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 9:
    conceito = "A"
    print(f"\nConceito: {conceito}, APROVADO.\n")
elif media >= 7.5 and media < 9:
    conceito = "B"
    print(f"\nConceito: {conceito}, APROVADO.\n")
elif media >= 6 and media < 7.5:
    conceito = "C"
    print(f"\nConceito: {conceito}, APROVADO.\n")
elif media >= 4 and media < 6:
    conceito = "D"
    print(f"\nConceito: {conceito}, REPROVADO.\n")
else:
    conceito = "F"
    print(f"\nConceito: {conceito}, BURRO.\n")