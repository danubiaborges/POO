import tkinter as tk
from tkinter import messagebox
import album as alb


class Artista:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


class LimiteCadastraArtista(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Artista")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelNome.pack(side="left")

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class LimiteConsultaArtista(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title('Consultar artista')
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()

        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelNome.pack(side="left")

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton, text="Consultar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class CtrlArtista():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaArtista = [ Artista('Dudu do Sertão'),
        Artista('Guilherme'),
        Artista('Jão')

        ]

    
    def getArtista(self, nome):
        artRet = None
        for art in self.listaArtista:
            if art.nome == nome:
                artRet = art
        return artRet

    
    def listaArtistas (self):
        return self.listaArtista

    def listaArtistasNome (self):
        listaArtistasNomes = []
        for art in self.listaArtista:
            listaArtistasNomes.append(art.nome)
        return listaArtistasNomes


    def cadastraArtista(self):
        self.limiteIns = LimiteCadastraArtista(self)

    def consultaArtista(self):
        self.limiteConsulta = LimiteConsultaArtista(self)

    def enterHandler(self, event):
        nome = self.limiteIns.inputNome.get()
        artista = Artista(nome)
        self.listaArtista.append(artista)
        self.limiteIns.mostraJanela('Sucesso', 'Artista cadastrado com sucesso')
        self.clearHandler(event)

    def consultHandler(self, event):
        listaAlbum = self.ctrlPrincipal.ctrlAlbum.getListaAlbuns()
        listaMusicasAlbum = self.ctrlPrincipal.ctrlAlbum.listaMusicasAlbum
        artista = self.limiteConsulta.inputNome.get()
        str = ''
        for art in self.listaArtista:
            if artista == art.nome:
                str += 'Artista: ' + art.nome + '\n'
                for album in listaAlbum:
                    if artista == album.artista:
                        str += 'Álbum nome: ' + album.titulo + '\n'
                        str += 'Músicas: ' +'\n'
                        for musica in listaMusicasAlbum:
                            str += musica + '\n'
        self.limiteConsulta.mostraJanela('Sucesso!', str)


    def clearHandler(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()
