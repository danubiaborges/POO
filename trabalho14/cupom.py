import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os.path
import pickle

class CupomFiscal():
    def __init__(self, nroCupom):
        self.__nroCupom = nroCupom
        self.__itensCupom = []

    @property
    def nroCupom(self):
        return self.__nroCupom

    @property
    def itens(self):
        return self.__itensCupom

    def addItens(self, item):
        self.__itensCupom.append(item)

class cadastrarCupomFiscal(tk.Toplevel):
    def __init__(self, ctrl, ctrlProduto):
        tk.Toplevel.__init__(self)
        self.geometry('500x150')
        self.title("Gerar Cupom Fiscal")

        self.frameCodigo = tk.Frame(self)
        self.frameProduto = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameCodigo.pack()
        self.frameProduto.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text="Código: ")
        self.labelCodigo.pack(side="left")
        self.inputCodigo = tk.Entry(self.frameCodigo, width=40)
        self.inputCodigo.pack(side="left")

        self.labelProduto = tk.Label(self.frameProduto, text="Produto: ")
        self.labelProduto.pack(side="left")
        self.combo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameProduto, width=30, textvariable=self.combo)
        self.combobox.pack(side="left")
        self.combobox['values'] = ctrlProduto.getProdutosDesc()

        self.submitProduto = tk.Button(self.frameProduto, text="Cadastrar Produto")      
        self.submitProduto.pack(side="right")
        self.submitProduto.bind("<Button>", ctrl.enterCadastroProdutoCupom)

        self.submit = tk.Button(self.frameButton, text="Cadastrar")      
        self.submit.pack(side="left")
        self.submit.bind("<Button>", ctrl.enterCadastroCupomFiscal)

        self.submit = tk.Button(self.frameButton, text="Apagar")      
        self.submit.pack(side="left")
        self.submit.bind("<Button>", ctrl.clearCadastroCupomFiscal)

class consultarCupomFiscal(tk.Toplevel):
    def __init__(self, ctrl):
        tk.Toplevel.__init__(self)
        self.geometry('350x200')
        self.title("Localizar Cupom Fiscal")

        self.frameCodigo = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameCodigo.pack()
        self.frameButton.pack()  

        self.labelCodigo = tk.Label(self.frameCodigo, text="Código: ")
        self.labelCodigo.pack(side="left")
        self.inputCodigo = tk.Entry(self.frameCodigo, width=40)
        self.inputCodigo.pack(side="left")
        
        self.submit = tk.Button(self.frameButton, text="Localizar")      
        self.submit.pack(side="left")
        self.submit.bind("<Button>", ctrl.enterConsultaCupomFiscal)

        self.submit = tk.Button(self.frameButton, text="Apagar")      
        self.submit.pack(side="left")
        self.submit.bind("<Button>", ctrl.clearConsultaCupomFiscal)

class CtrlCupomFiscal():
    def __init__(self):
        if not os.path.isfile("cupom.pickle"):
            self.cupom = {}
        else:
            with open("cupom.pickle", "rb") as f:
                self.cupom = pickle.load(f)
        
        self.produtos = []

    def getCupomFiscal(self):
        return self.cupom

    def salvaCupomFiscal(self):
        if len(self.cupom) != 0:
            with open("cupom.pickle","wb") as f:
                pickle.dump(self.cupom, f)

    def cadastrarCupomFiscal(self, ctrlProduto):
        self.produtos = []
        self.ctrlProduto = ctrlProduto
        self.cadastro = cadastrarCupomFiscal(self, self.ctrlProduto)

    def consultarCupomFiscal(self):
        self.consulta = consultarCupomFiscal(self)

    def enterCadastroCupomFiscal(self, event):
        codigo = self.cadastro.inputCodigo.get()

        if codigo in self.cupom:
            messagebox.showinfo(title='Cupom fiscal existente', message='O cupom fiscal já está cadastrado!')
        else:
            self.cupom[codigo] = CupomFiscal(codigo)

            for produto in self.produtos:
                self.cupom[codigo].addItens(produto)

        self.produtos = []
        self.salvaCupomFiscal()
        self.clearCadastroCupomFiscal(event)

    def clearCadastroCupomFiscal(self, event):
        self.cadastro.inputCodigo.delete(0, len(self.cadastro.inputCodigo.get()))
        self.cadastro.combo.set('')

    def enterConsultaCupomFiscal(self, event):
        codigo = self.consulta.inputCodigo.get()
        total = 0

        if codigo in self.cupom:
            info = 'Código: ' + str(codigo) + '\nProdutos:\n'

            for produto in self.cupom[codigo].itens:
                total += produto.valor
                info += str(produto.codigo) + ' - ' + produto.descricao + ' - ' + str(produto.valor) + '\n'

            info += 'Total: {:.2f}'.format(total)

            messagebox.showinfo(title='Cupom fiscal encontrado', message=info)
        else:
            messagebox.showinfo(title='Cupom fiscal inexistente', message='Não foi possivel encontrar o cupom fiscal desejado!')

    def clearConsultaCupomFiscal(self, event):
        self.consulta.inputCodigo.delete(0, len(self.consulta.inputCodigo.get()))

    def enterCadastroProdutoCupom(self, event):
        codigo = self.cadastro.combo.get().split(' ')
        codigo = codigo[0]

        if self.ctrlProduto.getProduto(codigo) != False:
            self.produtos.append(self.ctrlProduto.getProduto(codigo))
            self.cadastro.combo.set('')