import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import artista as ast
import album as alb

class Playlist:

    def __init__(self, nome, artista, musicas):
        self.__nome = nome
        self.__musicas = musicas
        self.__artista = artista

    @property
    def nome (self):
        return self.__nome

    @property
    def artista (self):
        return self.__artista
    
    @property
    def musicas (self):
        return self.__musicas


class LimiteCadastraPlaylist(tk.Toplevel):
    def __init__(self, controle, listaArtistas, listaMusicas):

        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Playlist")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameMusica = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameArtista.pack()
        self.frameMusica.pack()
        self.frameButton.pack()        

        self.labelNome = tk.Label(self.frameNome,text="Informe o nome da Playlist: ")
        self.labelNome.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        self.labelArtista = tk.Label(self.frameArtista,text="Escolha o Artista: ")
        self.labelArtista.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameArtista, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaArtistas
          
        self.labelMusica = tk.Label(self.frameMusica,text="Escolha a música: ")
        self.labelMusica.pack(side="left") 
        self.listbox = tk.Listbox(self.frameMusica)
        self.listbox.pack(side="left")
        for msc in listaMusicas:
            self.listbox.insert(tk.END, msc)

        self.buttonInsere = tk.Button(self.frameButton ,text="Insere Música")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereMusica)

        self.buttonCria = tk.Button(self.frameButton ,text="Cria Playlist")           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaPlaylist)    

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)            

class LimiteConsultaPlaylist(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title('Consultar Playlist')
        self.controle = controle
        self.frameCodigo = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameButton.pack()
        self.labelMatricula = tk.Label(self.frameCodigo, text="Nome da Playlist: ")
        self.labelMatricula.pack(side="left")
        
        self.inputNome = tk.Entry(self.frameCodigo, width=20)
        self.inputNome.pack(side="left")
        
        self.buttonSubmit = tk.Button(self.frameButton ,text="Consultar")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultHandler)

    
    def mostraJanela(self, titulo, msg):
      messagebox.showinfo(titulo, msg)

class CtrlPlaylist():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaPlaylist = [ Playlist('Parachutes', 'Coldplay', 'Sparks, Yellow')

        ]
        self.listaMusicasPlaylist = ['Sparks, Yellow']

    def cadastraPlaylist(self):        
        listaArtistas = self.ctrlPrincipal.ctrlArtista.listaArtistasNome()
        listaMusicas = self.ctrlPrincipal.ctrlAlbum.listaMusicas
        self.limiteIns = LimiteCadastraPlaylist(self, listaArtistas, listaMusicas)

    def criaPlaylist(self, event):
        nomePlaylist = self.limiteIns.inputNome.get()
        artSel = self.limiteIns.escolhaCombo.get()
        artista = self.ctrlPrincipal.ctrlAlbum.getTitulo(artSel)
        playlist = Playlist(nomePlaylist, artista, self.listaMusicasPlaylist)
        self.listaPlaylist.append(playlist)
        self.limiteIns.mostraJanela('Sucesso', 'Playlist criada com sucesso')
        self.limiteIns.destroy()


    def consultaPlaylist(self):
        self.limiteConsulta = LimiteConsultaPlaylist(self)

    def insereMusica(self, event):
        mscSel = self.limiteIns.listbox.get(tk.ACTIVE)
        musica = self.ctrlPrincipal.ctrlAlbum.getMusica(mscSel)
        self.listaMusicasPlaylist.append(musica)
        self.limiteIns.mostraJanela('Sucesso', 'Musica cadastrada')
        self.limiteIns.listbox.delete(tk.ACTIVE)

    def consultHandler (self, event):
        str = ''
        Nome = self.limiteConsulta.inputNome.get()
        for nomep in self.listaPlaylist:
            if Nome == nomep.nome:
                str += 'Título da Playlist: ' + Nome + '\n'
                str += 'Músicas: ' + '\n'
                for msc in self.listaMusicasPlaylist:
                    str += msc + '\n'
        self.limiteConsulta.mostraJanela('Consulta', str)
