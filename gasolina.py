def calculo(p_valorpgto, p_precolitro):
    res = p_valorpgto / p_precolitro
    return  res

nome = input("Informe seu nome: ")
precolitro = float(input("Informe o valor por litro de gasolina: "))
valorpgto = float(input("Informe o valor de pagamento: "))

res= calculo(precolitro, valorpgto)
print(f"{nome}, voce vai abastacer {res:.3f} litros de gasolina")