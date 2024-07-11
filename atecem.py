def conta(x):
    if x <= 100:
        print(x)
        conta(x + 1)

num = int(input("Informe um numero para ir dele até 100: "))

conta(num)