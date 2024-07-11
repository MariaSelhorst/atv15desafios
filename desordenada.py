val = [0] * 10
busca =  0
achou = 0
count = 0 

for count in range(10):
    val[count] = int(input(f"Informe o {count+1}° valor: "))

busca = int(input("Informe um valor para ser procurado: "))

for count in range(10):
    if busca == val[count]:
        achou = achou + 1


print(f"O numero foi encontrado {achou} vezes.")