import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import cupom as cup
import produto as prod

class Main():
    def __init__(self, root, controle):
        self.ctrl = controle
        self.root = root
        self.root.geometry('400x250')

        self.menu = tk.Menu(self.root)
        self.produto = tk.Menu(self.menu)
        self.cupom = tk.Menu(self.menu)

        self.produto.add_command(label="Criar Produto", command=self.ctrl.cadastrarProduto)
        self.produto.add_command(label="Localizar Produto", command=self.ctrl.consultarProduto)
        self.menu.add_cascade(label="Produto", menu=self.produto)

        self.cupom.add_command(label="Gerar Cupom Fiscal", command=self.ctrl.cadastrarCupom)
        self.cupom.add_command(label="Localizar Cupom Fiscal", command=self.ctrl.consultarCupom)
        self.menu.add_cascade(label="Cupom Fiscal", menu=self.cupom)

        self.root.config(menu=self.menu)

class CtrlPrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlProduto = prod.CtrlProduto()
        self.ctrlCupomFiscal = cup.CtrlCupomFiscal()

        self.main = Main(self.root, self)
        
        self.root.title("Cupom Fiscal")
        self.root.mainloop()

    def cadastrarProduto(self):
        self.ctrlProduto.cadastrarProduto()

    def consultarProduto(self):
        self.ctrlProduto.consultarProduto()

    def cadastrarCupom(self):
        self.ctrlCupomFiscal.cadastrarCupomFiscal(self.ctrlProduto)

    def consultarCupom(self):
        self.ctrlCupomFiscal.consultarCupomFiscal()

if __name__ == '__main__':
    CtrlPrincipal()