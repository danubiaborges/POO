# Numa certa universidade, cada aluno está matriculado em um curso de graduação. Por
# efeito de simplificação, cada curso possui exatamente uma grade, a qual agrega as
# disciplinas do curso. Os alunos podem cursar quaisquer disciplinas, estejam elas na
# grade de seu curso ou na grade de outro curso. As disciplinas cursadas que fazem parte
# da grade de seu curso contam como disciplinas obrigatórias, já as disciplinas cursadas
# de outros cursos contam como disciplinas eletivas.
# Implemente o modelo a seguir de forma a permitir que uma instância da classe
# Historico contenha uma lista com as disciplinas cursadas pelo aluno (o aluno,
# obviamente, deve ser instanciado). Seu programa deve processar o histórico e
# informar a carga horária total das disciplinas obrigatórias cursadas e a carga horária
# total das disciplinas eletivas cursadas.
# Você deve criar ao menos dois cursos e duas grades para poder testar seu código. 


class Aluno:
    def __init__(self, nome, matricula, historico, grade):
        self.__nome = nome
        self.__matricula = matricula
        self.__historico = historico
        self.__grade = grade

    def getNome(self):
        return self.__nome

    def getMatricula(self):
        return self.__matricula

    def getHistorico(self):
        return self.__historico

    def getGrade(self):
        return self.__grade

    def exibe(self):
        print('\n\nAluno(a): {} - Matricula: {}'.format(self.__nome, self.__matricula))
        print('\nLista de Disciplinas do Historico: ')
        lista = self.__historico.getListaDisc()
        grade = self.__grade.getListaDisc()
        obrigatoria = 0
        eletiva = 0
        for i in lista:
            encontrou = False
            print('Codigo: {} - Disciplina: {} - Carga Horaria: {}'.format(i.getCodigo(), i.getNome(), i.getCargaHoraria()))
            for j in grade:
                if i.getCodigo() == j.getCodigo():
                    obrigatoria += i.getCargaHoraria()
                    encontrou = True
            if(encontrou == False):
                eletiva += i.getCargaHoraria()
        print('Total de carga horaria obrigatoria: {} \nTotal de carga horaria eletiva: {}\n'.format(obrigatoria, eletiva)) 

class Curso:
    def __init__(self, nome, listaAlunos, grade):
        self.__nome = nome
        self.__listaAlunos = listaAlunos
        self.__grade = grade

    def getNome(self):
        return self.__nome

    def getListaAlunos(self):
        return self.__listaAlunos

    def getGrade(self):
        return self.__grade

    def exibe(self):
        print('Curso: {} \nGrade: Ano(a):{}'.format(self.__nome, self.__grade.getAno()))
        print('\nLista de Disciplinas: ')
        listaDisc = self.__grade.getListaDisc()
        for i in listaDisc:
            print('Codigo: {} - Disciplina: {} - Carga Horaria: {}'.format(i.getCodigo(), i.getNome(), i.getCargaHoraria()))
        print('Lista dos Alunos: ')
        listaAlunos = self.__listaAlunos
        for i in listaAlunos:
            print('Matricula: {} - Aluno: {}'.format(i.getMatricula(), i.getNome()))

class Grade:
    def __init__(self, ano, listaDisc):
        self.__ano = ano
        self.__listaDisc = listaDisc

    def getAno(self):
        return self.__ano
    
    def getListaDisc(self):
        return self.__listaDisc

    def exibe(self):
        print('Ano: {} \nLista de Disciplinas: '.format(self.__ano))
        lista = self.__listaDisc
        for i in lista:
            print('Codigo: {} - Disciplina: {} - Carga Horaria: {}'.format(i.getCodigo(), i.getNome(), i.getCargaHoraria()))

class Disciplina:
    def __init__(self, codigo, nome, cargaHoraria):
        self.__codigo = codigo
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria

    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.__nome

    def getCargaHoraria(self):
        return self.__cargaHoraria

    def __str__(self):
        return 'Codigo: {} - Disciplina: {} - Carga Horaria: {}'.format(self.__codigo, self.__nome, self.__cargaHoraria)

class Historico:
    def __init__(self, listaDisc):
        self.__listaDisc = listaDisc
    
    def getListaDisc(self):
        return self.__listaDisc

    def exibe(self):
        print('\nLista de Disciplinas do Historico: ')
        lista = self.__listaDisc
        for i in lista:
            print('Codigo: {} - Disciplina: {} - Carga Horaria: {}'.format(i.getCodigo(), i.getNome(), i.getCargaHoraria()))

# Adicionando Disciplinas
disc1 = Disciplina('COM310', 'Metodologia Cientifica Para Informatica', 32)
disc2 = Disciplina('COM110', 'Fundamentos de Programacao', 80)
disc3 = Disciplina('CIC310', 'Economia da Informacao', 48)
disc4 = Disciplina('MAT015', 'Matematica Discreta', 64)
disc5 = Disciplina('CIC132', 'Linguagens Formais e Automatos', 64)
disc6 = Disciplina('CIC271', 'Processamento Digital de Imagens', 64)
disc7 = Disciplina('COM921', 'Banco de Dados', 64)
disc8 = Disciplina('SIN411', 'Comportamento Organizacional', 48)
disc9 = Disciplina('SIN310', 'Introducao a Administracao', 64)
disc10 = Disciplina('SIN260', 'Sistemas Inteligentes', 64)

# Grade SIN - 2013
listaGradeSin = [disc1, disc2, disc3, disc4, disc7, disc8, disc9, disc10]
gradeSin = Grade(2013, listaGradeSin)

# Grade CCO - 2013
listaGradeCco= [disc1, disc2, disc3, disc4, disc5, disc6, disc7]
gradeCco = Grade(2013, listaGradeCco)

# Historicos
listaCursadas1 = [disc1, disc2, disc3, disc4, disc5, disc6, disc7, disc8, disc9, disc10]
historico1 = Historico(listaCursadas1)

listaCursadas2 = [disc1, disc2, disc3, disc4, disc5]
historico2 = Historico(listaCursadas2)

listaCursadas3 = [disc6, disc7, disc8, disc9, disc10]
historico3 = Historico(listaCursadas3)

listaCursadas4 = [disc3, disc4, disc5, disc6, disc7]
historico4 = Historico(listaCursadas4)

listaCursadas5 = [disc1, disc2, disc8, disc9, disc10]
historico5 = Historico(listaCursadas5)

aluno1 = Aluno('Hermione', 12038, historico1, gradeSin)
aluno2 = Aluno('Harry', 40938, historico2, gradeCco)
aluno3 = Aluno('Ron', 47326, historico3, gradeCco)
aluno4 = Aluno('Draco', 34268, historico4, gradeCco)
aluno5 = Aluno('Luna', 23498, historico5, gradeSin)

listaAlunosSin = [aluno1, aluno2, aluno5]
cursoSin = Curso('Sistemas de Informacao', listaAlunosSin, gradeSin)

listaAlunosCco = [aluno3, aluno4]
cursoCco = Curso('Ciencia da Computacao', listaAlunosCco, gradeCco)

aluno1.exibe()
aluno2.exibe()
aluno3.exibe()
aluno4.exibe()
aluno5.exibe()