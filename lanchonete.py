

print("\n-----------MENU----------")
print("|1. Cardapio\t\t|")
print("|2. Fazer Pedido\t|")
print("------------------------")

op = int(input("\nDigite a opção desejada? "))

if op == 1:
    print("\n------------CARDAPIO-----------")
    print("|cod \tproduto\t\tpreço |")
    print("|100 \tsanduiche veg\t 1.20 |")
    print("|101 \tx-burguer\t 1.30 |")
    print("|102 \tx-salada\t 1.50 |")
    print("|103 \tx-tudo\t\t 1.70 |")
    print("|201 \tagua\t\t 1.20 |")
    print("|202 \trefrigerante\t 1.50 |")
    print("|203 \tcafé\t\t 0.70 |")
    print("-------------------------------")

else:
    cod1 = float(input("\nDigite o cod do lache: "))
    cod2 = float(input("\nDigite o cod da bebida: "))
    

    if cod1 == 100:
        lanche = 1.20
        print("\nR$ 1.20")
    elif cod1 == 101:
        lanche = 1.30
        print("\nR$ 1.30")
    elif cod1 == 102:
        lanche = 1.50
        print("\nR$ 1.50")
    elif cod1 == 103:
        lanche = 1.70
        print("\nR$ 1.70")
    else:
        print("cod incorreto.")

    if cod2 == 201:
        bebida = 1.20
        print("\nR$ 1.20")
    elif cod2 == 202:
        bebida = 1.50
        print("\nR$ 1.50")
    elif cod2 == 203:
        bebida = 0.70
        print("\nR$ 0.70")
    else:
        print("cod incorreto")


    pagar = lache = bebida

    print(f"\nTOTAL A PAGAR: {pagar:.2f}\n")