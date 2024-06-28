x = 0
salL = 0
salIR = 0
valorINSS = 0
valorIR = 0
somaINSS = 0
somaIR = 0

cod = input("Digite o codigo do funcionario: ")
dep = int(input("Digite o numero de dependentes: "))  

for x in range(12):
    salB = float(input(f"Digite o salario bruto do mês {x+1}: "))  
    if salB <= 1399.12:
        valorINSS = salB * 0.08
        somaINSS += valorINSS
        salL = salB - (salB * 0.08)
    elif salB <= 2331.88:
        valorINSS = salB * 0.09
        somaINSS += valorINSS
        salL = salB - (salB * 0.09)
    elif salB <= 4663.75:
        valorINSS = salB * 0.11
        somaINSS += valorINSS
        salL = salB - (salB * 0.11)
    else:
        valorINSS = 513.01
        somaINSS += valorINSS
        salL = salB - 513.01

    if dep >= 1:
        salIR = salL - (dep * 189.59)
    else:
        salIR = salL

    if salIR <= 1903.98:
        valorIR = 0
        somaIR += valorIR
    elif salIR <= 2826.65:
        valorIR = ((salIR * 0.075) - 142.80)
        somaIR += valorIR
    elif salIR <= 3751.05:
        valorIR = ((salIR * 0.15) - 354.80)
        somaIR += valorIR
    elif salIR <= 4664.68:
        valorIR = ((salIR * 0.225) - 636.13)
        somaIR += valorIR
    else:
        valorIR = ((salIR * 0.275) - 869.36)
        somaIR += valorIR

    salL = salL - valorIR 

    print(f"Salario Liquido= %.2f" % salL) 
    print(f"Valor INSS= %.2f" % valorINSS)
    print(f"Valor IR= %.2f\n" % valorIR)

print(f"Funcionario: {cod}")
print(f"Valor no ano a pagar de INSS= {somaINSS}")
print(f"Valor no ano a pagar de IR= {somaIR}")
