# Caio Miranda - 2021024231
import tkinter as tk
import Equipe as equip
from tkinter import ttk
from tkinter import messagebox
import pickle
import os.path

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.equipeMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)

        self.equipeMenu.add_command(label="Criar equipe", command=self.controle.criarEquipe)
        self.equipeMenu.add_command(label="Consultar equipe", command=self.controle.consultarEquipe)
        self.equipeMenu.add_command(label="Imprimir Dados", command=self.controle.imprimirDados)
        self.menubar.add_cascade(label="Equipe", menu=self.equipeMenu)

        self.sairMenu.add_command(label="Salva", command=self.controle.salvaDados)
        self.menubar.add_cascade(label="Sair", menu=self.sairMenu)
               
        self.root.config(menu=self.menubar)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlEquipe = equip.CtrlEquipe(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Campeonato")
        # Inicia o mainloop
        self.root.mainloop()
    
    def criarEquipe(self):
        self.ctrlEquipe.criarEquipe()
    
    def consultarEquipe(self):
        self.ctrlEquipe.consultarEquipe()
    
    def imprimirDados (self):
        self.ctrlEquipe.imprimirDados()
    
    def salvaDados(self):
        self.ctrlEquipe.salvaEquipe()
        self.root.destroy()


if __name__ == '__main__':
    c = ControlePrincipal()