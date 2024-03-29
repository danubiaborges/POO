import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class ModelCliente():
    def __init__(self, nome, email, codigo):
        self.__nome = nome
        self.__email = email
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def codigo(self):
        return self.__codigo

class View():
    def __init__(self, master, controller):
        self.controller = controller
        self.janela = tk.Frame(master)
        self.janela.pack()
        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)
        self.frame3 = tk.Frame(self.janela)
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
      
        self.labelInfo1 = tk.Label(self.frame1, text="Nome: ")
        self.labelInfo2 = tk.Label(self.frame2, text="Email: ")
        self.labelInfo3 = tk.Label(self.frame3, text="Codigo: ")
        self.labelInfo1.pack(side="left")
        self.labelInfo2.pack(side="left") 
        self.labelInfo3.pack(side="left") 

        self.inputText1 = tk.Entry(self.frame1, width=20)
        self.inputText1.pack(side="left")
        self.inputText2 = tk.Entry(self.frame2, width=20)
        self.inputText2.pack(side="left")             
        self.inputText3 = tk.Entry(self.frame3, width=20)
        self.inputText3.pack(side="left") 

        self.buttonSubmit = tk.Button(self.janela,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controller.enterHandler)
      
        self.buttonClear = tk.Button(self.janela,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controller.clearHandler)  

        self.buttonListar = tk.Button(self.janela, text = "Listar")
        self.buttonListar.pack(side = "left")
        self.buttonListar.bind("<Button>", controller.listarHandler)  

        self.buttonConsultar = tk.Button(self.janela, text = "Consultar")
        self.buttonConsultar.pack(side = "left")
        self.buttonConsultar.bind("<Button>", controller.consultarHandler)         

    def mostraJanela(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)
      
class Controller():       
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x100')
        self.listaClientes = []

        # Cria a view passando referência da janela principal e
        # de si próprio (controlador)
        self.view = View(self.root, self) 

        self.root.title("Exemplo MVC")
        # Inicia o mainloop
        self.root.mainloop()

    def enterHandler(self, event):
        nomeCli = self.view.inputText1.get()
        emailCli = self.view.inputText2.get()
        codigoCli = self.view.inputText3.get()
        cliente = ModelCliente(nomeCli, emailCli, codigoCli)
        self.listaClientes.append(cliente)
        self.view.mostraJanela('Sucesso', 'Cliente cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.view.inputText1.delete(0, len(self.view.inputText1.get()))
        self.view.inputText2.delete(0, len(self.view.inputText2.get()))
        self.view.inputText3.delete(0, len(self.view.inputText3.get()))

    def listarHandler(self, event):
        self.msg = "Clientes cadastrados:\n"
        for cliente in self.listaClientes:
            self.msg += cliente.nome + ' - ' +cliente.email + '\n'
        self.view.mostraJanela('Listagem de clientes', self.msg)

    def consultarHandler(self, event):
        answer = simpledialog.askstring("Código", "Insira o código do cliente: ")
        for cliente in self.listaClientes:
            self.msg = 'Cliente: '
            if answer == str(cliente.codigo):
                self.msg += cliente.nome + ' - ' + cliente.email + ' - ' + cliente.codigo + '\n'
                self.view.mostraJanela('Consulta', self.msg)
                break
        else:
            self.msg = 'Código não cadastrado.'
            self.view.mostraJanela('Consulta', self.msg)

if __name__ == '__main__':
    c = Controller()