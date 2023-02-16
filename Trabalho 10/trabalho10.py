from abc import ABC, abstractmethod

class TitulacaoInvalida(Exception):
    pass

class IdadeProfInvalida(Exception):
    pass

class CursoIvalido(Exception):
    pass

class IdadeAlunoInvalida(Exception):
    pass

class CpfInvalido(Exception):
    pass

class Pessoa(ABC):
    def __init__(self, nome, end, idade, cpf):
        self.__nome = nome
        self.__end = end
        self.__idade = idade
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def end(self):
        return self.__end

    @property
    def idade(self):
        return self.__idade

    @property
    def cpf(self):
        return self.__cpf

    @abstractmethod
    def printDescricao(self):
        pass

class Professor(Pessoa):
    def __init__(self, nome, end, idade, cpf, titulacao):
        super().__init__(nome, end, idade, cpf)
        self.__titulacao = titulacao

    @property
    def titulacao(self):
        return self.__titulacao

    def printDescricao(self):
        print("Nome: {}".format(self.nome))
        print("Endereço: {}".format(self.end))
        print("Idade: {}".format(self.idade))
        print("CPF: {}".format(self.cpf))
        print("Titulação: {}".format(self.titulacao))

class Aluno(Pessoa):
    def __init__(self, nome, end, idade, cpf, curso):
        super().__init__(nome, end, idade, cpf)
        self.__curso = curso

    @property
    def curso(self):
        return self.__curso

    def printDescricao(self):
        print("Nome: {}".format(self.nome))
        print("Endereço: {}".format(self.end))
        print("Idade: {}".format(self.idade))
        print("CPF: {}".format(self.cpf))
        print("Curso: {}".format(self.curso))


if __name__ == "__main__":

        prof1 = Professor("Luiz", "BPS", 29, 49822, "Doutor")               # vai falhar, pois idade < 30
        prof2 = Professor("Inacio", "Pinheirinho", 31, 42030, "Doutor")     # OK
        prof3 = Professor("Fernando", "Varginha", 32, 12093, "Mestre")      # vai falhar, pois prof != doutor
        prof4 = Professor("Guilherme", "Centro", 38, 90155, "Doutor")       # vai falhar, pois cpf = aluno4
        aluno1 = Aluno("Fernanda", "Centro", 17, 29282, "CCO")              # vai falhar, pois idade < 18
        aluno2 = Aluno("Bruna", "Varginha", 19, 19320, "SIN")               # OK
        aluno3 = Aluno("Letícia", "BPS", 20, 39018, "ECO")                  # vai falhar, pois curso não é SIN ou CCO
        aluno4 = Aluno("Gabriela", "Pinheirinho", 22, 90155, "SIN")         # vai falhar, pois cpf = prof4

        listaAlunos = [aluno1, aluno2, aluno3, aluno4]
        listaProfs = [prof1, prof2, prof3, prof4]
        cadastro = []
        cadastroCpf = {}

        print("******************** ERRO ********************")

        for aluno in listaAlunos:

            try:
                if aluno.cpf in cadastroCpf:
                    raise CpfInvalido
                if aluno.idade < 18:
                    raise IdadeAlunoInvalida
                if aluno.curso != "SIN" and aluno.curso != "CCO":
                    raise CursoIvalido
                else:
                    cadastroCpf[aluno.cpf] = aluno
                    cadastro.append(aluno)

            except CpfInvalido:
                print("O CPF do aluno é repetido: %d" % aluno.cpf)
            except IdadeAlunoInvalida:
                print("Idade de aluno inválida: %d" % aluno.idade)
            except CursoIvalido:
                print("Curso inválido: %s" % aluno.curso)

            print()

        for prof in listaProfs:

            try:
                if prof.cpf in cadastroCpf:
                    raise CpfInvalido
                if prof.idade < 30:
                    raise IdadeProfInvalida
                if prof.titulacao != "Doutor":
                    raise TitulacaoInvalida
                else:
                    cadastroCpf[prof.cpf] = prof
                    cadastro.append(prof)

            except CpfInvalido:
                print("O CPF do professor é repetido: %d" % prof.cpf)
            except IdadeProfInvalida:
                print("Idade de professor inválida: %d" % prof.idade)
            except TitulacaoInvalida:
                print("Titulação inválida: %s" % prof.titulacao)

        print()

        print("******************** Pessoas Cadastradas ********************")
        for pessoa in cadastro:
            pessoa.printDescricao()
            print()