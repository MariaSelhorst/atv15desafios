def soma(x, y):
    if y == 1:
        return x
    else:
        return x + soma(x, y -1)
    
multiplicando = int(input("Informe o multiplicando: "))
multiplicador = int(input("Informe o multiplicador: "))

produto = soma(multiplicando, multiplicador)

print(f"Soma do multiplicando pelo número de vezes do muliplicador é: {produto}")

