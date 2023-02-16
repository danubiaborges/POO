import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pickle
import os.path

class Curso():
    def __init__(self, sigla, nome):
        self.__sigla = sigla
        self.__nome = nome
    
    @property
    def sigla (self):
        return self.__sigla
    
    @property
    def nome (self):
        return self.__nome

class Estudante():
    def __init__(self, nroMatric, nome, curso):
        self.__nroMatric = nroMatric
        self.__nome = nome
        self.__curso = curso

    @property
    def nroMatric(self):
        return self.__nroMatric
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def curso(self):
        return self.__curso

class Equipe():
    def __init__(self, curso):
        self.__curso = curso
        self.__listaEstudantes = []
    
    @property
    def curso(self):
        return self.__curso
    
    @property
    def listaEstudantes(self):
        return self.__listaEstudantes
    
    @listaEstudantes.setter
    def listaEstudantes (self, aluno):
        self.__listaEstudantes.append(aluno)
    

class LimiteCriarEquipe(tk.Toplevel):
    def __init__(self, controle, listaCursos):

        tk.Toplevel.__init__(self)
        self.geometry('250x250')
        self.title("Criar equipe")
        self.frameNroMatric = tk.Frame(self)
        self.frameCurso = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCurso.pack()
        self.frameNroMatric.pack()
        self.frameButton.pack()

        
        self.labelCurso = tk.Label(self.frameCurso, text="Escolha o curso: ")
        self.labelCurso.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameCurso, width=30, textvariable=self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaCursos

        self.labelNroMatric = tk.Label(self.frameNroMatric, text="Número da matrícula: ")
        self.labelNroMatric.pack(side="left")
        self.inputNro = tk.Entry(self.frameNroMatric, width=20)
        self.inputNro.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Insere Aluno")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.insereAluno)

        self.buttonCria = tk.Button(self.frameButton ,text="Cria Equipe")           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaEquipe)    

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class LimiteImprimirDados():
    def __init__(self, str):
        messagebox.showinfo('Dados do campeonato', str)


class LimiteConsultaEquipe(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Consultar")
        self.controle = controle

        self.frameCurso = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCurso.pack()
        self.frameButton.pack()

        self.labelCurso = tk.Label(self.frameCurso, text="Sigla do Curso: ")
        self.labelCurso.pack(side="left")
        self.inputCurso = tk.Entry(self.frameCurso, width=20)
        self.inputCurso.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", self.controle.enterConsultHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", self.controle.fechaConsultHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class CtrlEquipe():
    def __init__(self, controlador):
        self.controlador = controlador
        c1 = Curso("CCO", "Ciência da Computação")
        c2 = Curso("SIN", "Sistemas de Informação")
        c3 = Curso("EEL", "Engenharia Elétrica")
        self.listaCurso = []
        self.listaCurso.append(c1)
        self.listaCurso.append(c2)
        self.listaCurso.append(c3)
        #Inserir mais cursos, se quiser
        self.listaEstudante = []
        self.listaEstudante.append(Estudante(1001, "Bruno", c1))
        self.listaEstudante.append(Estudante(1002, "Fernando", c1))
        self.listaEstudante.append(Estudante(1003, "Tiago", c2))
        self.listaEstudante.append(Estudante(1004, "Rafaela", c2))
        self.listaEstudante.append(Estudante(1005, "Maria Fernanda", c3))
        self.listaEstudante.append(Estudante(1006, "Bruna", c3))
        self.listaEstudante.append(Estudante(1007, "Caio", c2))
        self.listaEstudante.append(Estudante(1008, "Fernanda", c2))
        self.listaEstudante.append(Estudante(1009, "Diego", c1))
        self.listaEstudante.append(Estudante(1010, "Guilherme", c3))
        #Inserir mais 7 alunos, totalizando pelo menos 10 na lista
        if not os.path.isfile("equipes.pickle"):
            self.listaEquipes = []
        else:
            with open("equipes.pickle", "rb") as f:
                self.listaEquipes = pickle.load(f)

    def salvaEquipe(self):
        if len(self.listaEquipes) != 0:
            with open("equipes.pickle", "wb") as f:
                pickle.dump(self.listaEquipes, f)

    def getCurso(self, curso):
        cursoRet = None
        for formacao in self.listaCurso:
            if formacao.nome == curso:
                cursoRet = formacao
        return cursoRet
    
    def getEstudante(self, nroMatricula):
        estRet = None
        for alunos in self.listaEstudante:
            if alunos.nroMatric == nroMatricula:
                estRet = alunos
        return estRet

    def criarEquipe(self):
        listaCursoNome = []
        for curso in self.listaCurso:
            listaCursoNome.append(curso.nome)
        self.limiteIns = LimiteCriarEquipe(self, listaCursoNome)


    def insereAluno(self, event):
        nroMatricula = int(self.limiteIns.inputNro.get())
        cursoSel = self.limiteIns.escolhaCombo.get()
        formacao = self.getCurso(cursoSel)
        self.equipe = Equipe(formacao)
        aux = 0
        for aluno in self.listaEstudante:
            if nroMatricula == aluno.nroMatric:
                if formacao.nome == aluno.curso.nome:
                    aux = 1
                    estudante = self.getEstudante(nroMatricula)
                    self.equipe.listaEstudantes = estudante
                    self.limiteIns.mostraJanela('Sucesso', 'Aluno matriculado')
        if aux == 0:
            self.limiteIns.mostraJanela('Erro', 'Código de matrícula inexistente ou curso não correspondido')
            

    def criaEquipe(self, event):
        self.listaEquipes.append(self.equipe)
        self.limiteIns.mostraJanela('Sucesso', 'Equipe criada!')
        self.limiteIns.destroy()

    def consultarEquipe(self):
        self.limiteCons = LimiteConsultaEquipe(self)
    
    def enterConsultHandler(self, event):
        str = ''
        sigla = self.limiteCons.inputCurso.get()
        aux = 0
        for curso in self.listaCurso:
            if sigla == curso.sigla:
                aux = 1
                for equipe in self.listaEquipes:
                    if sigla == equipe.curso.sigla:
                        aux = 2
                        for eqp in equipe.listaEstudantes:
                            str += eqp.nome + '\n'
                    self.limiteCons.mostraJanela('Consulta', str)
        if aux == 0:
            self.limiteCons.mostraJanela('Erro', 'Nada foi encontrado!')
        if aux == 1:
            self.limiteCons.mostraJanela('Erro', 'Não existe equipe desse curso!')
        

    def imprimirDados(self):
        string = ''
        nroEst = 0
        for equipe in self.listaEquipes:
            nroEst += len(equipe.listaEstudantes)
        string += 'Número de equipes: ' + str(len(self.listaEquipes)) + '\n'
        string += 'Número de estudantes: ' + str(nroEst) + '\n'
        string += 'Média de estudantes por equipe: ' + str(nroEst/len(self.listaEquipes)) + '\n'
        self.limiteImp = LimiteImprimirDados(string)

    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def fechaConsultHandler(self, event):
        self.limiteCons.destroy()
