import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os.path
import pickle

class Produto():
    def __init__(self, codigo, descricao, valor):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valor = valor

    @property
    def codigo(self):
        return self.__codigo

    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def valor(self):
        return float(self.__valor)

class cadastrarProduto(tk.Toplevel):
    def __init__(self, ctrl):
        tk.Toplevel.__init__(self)
        self.geometry('350x200')
        self.title("Gerar Produto")

        self.frameCodigo = tk.Frame(self)
        self.frameDescricao = tk.Frame(self)
        self.framePreco = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameCodigo.pack()
        self.frameDescricao.pack()  
        self.framePreco.pack()
        self.frameButton.pack() 

        self.labelCodigo = tk.Label(self.frameCodigo, text="Código: ")
        self.labelCodigo.pack(side="left")
        self.inputCodigo = tk.Entry(self.frameCodigo, width=40)
        self.inputCodigo.pack(side="left")
        
        self.labelDescricao = tk.Label(self.frameDescricao, text="Descricao: ")
        self.labelDescricao.pack(side="left")
        self.inputDescricao = tk.Entry(self.frameDescricao, width=40)
        self.inputDescricao.pack(side="left")

        self.labelPreco = tk.Label(self.framePreco, text="Preço: ")
        self.labelPreco.pack(side="left")
        self.inputPreco = tk.Entry(self.framePreco, width=40)
        self.inputPreco.pack(side="left")

        self.submit = tk.Button(self.frameButton, text="Gerar")      
        self.submit.pack(side="left")
        self.submit.bind("<Button>", ctrl.enterCadastroProduto)

        self.submit = tk.Button(self.frameButton, text="Apagar")      
        self.submit.pack(side="left")
        self.submit.bind("<Button>", ctrl.clearCadastroProduto)

class consultarProduto(tk.Toplevel):
    def __init__(self, ctrl):
        tk.Toplevel.__init__(self)
        self.geometry('350x200')
        self.title("Localizar Produto")

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
        self.submit.bind("<Button>", ctrl.enterConsultaProduto)

        self.submit = tk.Button(self.frameButton, text="Apagar")      
        self.submit.pack(side="left")
        self.submit.bind("<Button>", ctrl.clearConsultaProduto)

class CtrlProduto:
    def __init__(self):
        if not os.path.isfile("produtos.pickle"):
            self.produtos = {}
        else:
            with open("produtos.pickle", "rb") as f:
                self.produtos = pickle.load(f)

    def getProdutosDesc(self):
        lista = []

        for codigo in self.produtos:
            lista.append(str(self.produtos[codigo].codigo) + ' - ' + self.produtos[codigo].descricao)

        return lista
    
    def getProduto(self, codigo):
        if codigo in self.produtos:
            return self.produtos[codigo]
        else:
            return False

    def salvaProdutos(self):
        if len(self.produtos) != 0:
            with open("produtos.pickle","wb") as f:
                pickle.dump(self.produtos, f)

    def cadastrarProduto(self):
        self.cadastro = cadastrarProduto(self)

    def consultarProduto(self):
        self.consulta = consultarProduto(self)

    def enterCadastroProduto(self, event):
        codigo = self.cadastro.inputCodigo.get()
        descricao = self.cadastro.inputDescricao.get()
        preco = self.cadastro.inputPreco.get()

        if codigo in self.produtos:
            messagebox.showinfo(title='Produto existente', message='O produto já está cadastrado!')
        else:
            self.produtos[codigo] = Produto(codigo, descricao, preco)
            self.salvaProdutos()
        
        self.clearCadastroProduto(event)

    def clearCadastroProduto(self, event):
        self.cadastro.inputCodigo.delete(0, len(self.cadastro.inputCodigo.get()))
        self.cadastro.inputDescricao.delete(0, len(self.cadastro.inputDescricao.get()))
        self.cadastro.inputPreco.delete(0, len(self.cadastro.inputPreco.get()))

    def enterConsultaProduto(self, event):
        codigo = self.consulta.inputCodigo.get()
        info = ''

        if codigo in self.produtos:
            info += 'Código: ' + str(self.produtos[codigo].codigo) + '\nDescrição: ' + self.produtos[codigo].descricao + '\nPreço: ' + str(self.produtos[codigo].valor)
            messagebox.showinfo(title='Produto Encontrado', message=info)
        else:
            messagebox.showinfo(title='Produto Inexistente', message='Não foi possivel encontrar o produto desejado!')

        self.clearConsultaProduto(event)

    def clearConsultaProduto(self, event):
        self.consulta.inputCodigo.delete(0, len(self.consulta.inputCodigo.get()))