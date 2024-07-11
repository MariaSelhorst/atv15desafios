def par_impar(p_num):
    if p_num % 2 == 0:
        print("PAR")
        return 'P'
    else:
        print("IMPAR")
        return 'I'

if __name__ == "__main__":

    num = int(input("Informe um número: "))
    
    resp = par_impar(num)
    print(resp)
