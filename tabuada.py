def Main():
    while True: 
        print("\n----------SISTEMA DE TABUADA----------")
        print("--------------------------------------")
        num_tabuada = print("\nDigite o numero da tabuada que gostaria de consultar ou digite 99 para sair: ")

        num_tabuada = int(input())

        if num_tabuada == 99:
            break

        if num_tabuada < 0 or num_tabuada > 10:
            print("\n----- Digite um numero de 1 a 10 ------")
        else:
            for count in range(1, 11):
                print(f"\n{num_tabuada} X {count} = {num_tabuada*count}")
    

if __name__ == "__main__":
    Main()