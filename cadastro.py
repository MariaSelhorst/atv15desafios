class Cadastro:
    def __init__(self):
        self.codigo = 0
        self.nome = ""
        self.telefone = 0
        self.email = ""

def main():
    aluno = Cadastro()

    aluno.codigo = int(input("\nInforme o codigo: "))
    aluno.nome = input("\nInforme o nome: ")
    aluno.telefone = int(input("\nInforme o telefone: "))
    aluno.email = input("\nInforme o email: ")

    print("\n****************************************************\n")
    print("**********************CADASTRO**********************\n")
    print("****************************************************\n")

    print(aluno.codigo)
    print(aluno.nome)
    print(aluno.telefone)
    print(aluno.email)

if __name__ == "__main__" :
    main()
