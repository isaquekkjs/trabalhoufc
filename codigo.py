class Aluno:
    def __init__(self, nome, media):
        self.nome = nome
        self.media = media
        self.atualizar_situacao()

    def atualizar_situacao(self):
        if self.media >= 7:
            self.situacao = "Aprovado"
        elif self.media >= 5:
            self.situacao = "Recuperação"
        else:
            self.situacao = "Reprovado"


class EscolaCE42:
    def __init__(self):
        self.alunos_ce42 = []

    def cadastrar(self):
        nome = input("Nome do aluno: ")
        media = float(input("Média do aluno: "))
        aluno = Aluno(nome, media)
        self.alunos_ce42.append(aluno)
        print("Aluno cadastrado!")

    def editar(self):
        nome = input("Nome atual do aluno: ")

        for aluno in self.alunos_ce42:
            if aluno.nome == nome:
                aluno.nome = input("Novo nome: ")
                aluno.media = float(input("Nova média: "))
                aluno.atualizar_situacao()
                print("Aluno atualizado!")
                return

        print("Aluno não encontrado!")

    def excluir(self):
        nome = input("Nome do aluno: ")

        for aluno in self.alunos_ce42:
            if aluno.nome == nome:
                confirmar = input("Deseja excluir? (s/n): ")

                if confirmar == "s":
                    self.alunos_ce42.remove(aluno)
                    print("Aluno excluído!")
                else:
                    print("Operação cancelada!")
                return

        print("Aluno não encontrado!")

    def listar(self, filtro="Todos"):
        print("\nNome | Média | Situação")

        for aluno in self.alunos_ce42:
            if filtro == "Todos" or aluno.situacao == filtro:
                print(aluno.nome, "|", aluno.media, "|", aluno.situacao)

    def filtrar(self):
        print("1 - Todos")
        print("2 - Aprovados")
        print("3 - Recuperação")
        print("4 - Reprovados")

        opcao = input("Escolha: ")

        if opcao == "1":
            self.listar()
        elif opcao == "2":
            self.listar("Aprovado")
        elif opcao == "3":
            self.listar("Recuperação")
        elif opcao == "4":
            self.listar("Reprovado")

    def salvar(self):
        arquivo = input("Nome do arquivo: ")

        with open(arquivo, "w") as f:
            for aluno in self.alunos_ce42:
                f.write(aluno.nome + "," + str(aluno.media) + "," + aluno.situacao + "\n")

        print("Dados salvos!")

    def carregar(self):
        arquivo = input("Nome do arquivo: ")

        try:
            with open(arquivo, "r") as f:
                for linha in f:
                    nome, media, situacao = linha.strip().split(",")
                    aluno = Aluno(nome, float(media))
                    self.alunos_ce42.append(aluno)

            print("Alunos carregados!")

        except FileNotFoundError:
            print("Arquivo não encontrado!")


escola = EscolaCE42()

while True:
    print("\n=== Cadastro Escolar CE-42 ===")
    print("1 - Cadastrar aluno")
    print("2 - Editar aluno")
    print("3 - Excluir aluno")
    print("4 - Listar alunos")
    print("5 - Filtrar alunos")
    print("6 - Salvar alunos")
    print("7 - Carregar alunos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        escola.cadastrar()
    elif opcao == "2":
        escola.editar()
    elif opcao == "3":
        escola.excluir()
    elif opcao == "4":
        escola.listar()
    elif opcao == "5":
        escola.filtrar()
    elif opcao == "6":
        escola.salvar()
    elif opcao == "7":
        escola.carregar()
    elif opcao == "0":
        print("Sistema encerrado!")
        break
    else:
        print("Opção inválida!")

