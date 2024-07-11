def mns(p_n1, p_nx_n1):
    if p_nx_n1 == 1:
        return p_n1
    else:
        return p_n1 + mns(p_n1, p_nx_n1-1)

n1 = int(input("Informe o primeiro número: "))
nx_n1 = int(input("Informe o numero de vezes que o 1° sera somado: "))

resp = mns(n1, nx_n1)
print(f"Resposta:{resp}")