import tkinter as tk
from tkinter import messagebox
import artista as art

class Album:

    def __init__(self, titulo, artista, ano, musicas):
        self.__titulo = titulo
        self.__artista = artista
        self.__ano = ano
        self.__musicas = musicas

    @property
    def titulo(self):
        return self.__titulo

    @property
    def artista(self):
        return self.__artista

    @property
    def ano (self):
        return self.__ano
    
    @property
    def musicas (self):
        return self.__musicas

class LimiteCadastraAlbum(tk.Toplevel):
    def __init__(self, controle, listaMusicas):

        tk.Toplevel.__init__(self)
        self.geometry('300x300')
        self.title("Album")
        self.controle = controle

        self.frameTitulo = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameMusicas = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameArtista.pack()
        self.frameTitulo.pack()
        self.frameAno.pack()
        self.frameMusicas.pack()
        self.frameButton.pack()
      
        self.labelArtista = tk.Label(self.frameArtista,text="Título: ")
        self.labelTitulo = tk.Label(self.frameTitulo,text="Nome do artista: ")
        self.labelAno = tk.Label(self.frameAno, text="Ano: ")
        self.labelMusicas = tk.Label(self.frameMusicas)
        self.labelArtista.pack(side="left")
        self.labelTitulo.pack(side="left")  
        self.labelAno.pack(side="left")
        self.labelMusicas.pack(side="left")

        self.inputArtista = tk.Entry(self.frameArtista, width=20)
        self.inputArtista.pack(side="left")
        self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
        self.inputTitulo.pack(side="left")    
        self.inputAno = tk.Entry(self.frameAno, width=20)
        self.inputAno.pack(side="left")

        self.labelMusica = tk.Label(self.frameMusicas,text="Escolha as músicas: ")
        self.labelMusica.pack(side="left") 
        self.listbox = tk.Listbox(self.frameMusicas)
        self.listbox.pack(side="left")
        for msc in listaMusicas:
            self.listbox.insert(tk.END, msc)


        self.buttonInsere = tk.Button(self.frameButton ,text="Insere Música")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereMusica)

        self.buttonSubmit = tk.Button(self.frameButton ,text="Cadastra album")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteCadastraMusica(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Musica")
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
        self.buttonSubmit.bind("<Button>", controle.enterMusicHandler)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaAlbum(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title('Consultar Album')
        self.controle = controle
        
        self.frameTitulo = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameTitulo.pack()
        self.frameButton.pack()
        
        self.labelTitulo = tk.Label(self.frameTitulo, text="Titulo: ")
        self.labelTitulo.pack(side="left")
        
        self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
        self.inputTitulo.pack(side="left")
        
        self.buttonSubmit = tk.Button(self.frameButton ,text="Consultar")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultHandler)

    def mostraJanela(self, titulo, msg):
      messagebox.showinfo(titulo, msg)

      
class CtrlAlbum():       
    def __init__(self):
        self.listaAlbuns = [ Album ('Anti-Heroi', 'Jão', 2019, 'Essa eu fiz pro nosso amor')
        
        ]

        self.listaMusicas = [ 'Sparks', 'Yellow'

        ]

        self.listaMusicasAlbum = [ 'Essa eu fiz pro nosso amor'

        ]

    
    def getListaAlbuns(self):
        return self.listaAlbuns
    

    def getTitulo(self, titulo):
        albRet = None
        for alb in self.listaAlbuns:
            if alb.titulo == titulo:
                albRet = alb
        return albRet

    def getMusica(self, nome):
        mscRet = None
        for msc in self.listaMusicas:
            if msc == nome:
                mscRet = msc
        return mscRet
    
    
    def listaMusica(self):
        return self.listaMusicas

    @property
    def ListaTituloAlbuns(self):
        listaTitulos = []
        for alb in self.listaAlbuns:
            listaTitulos.append(alb.getTitulo())
        return listaTitulos

    def cadastraAlbum(self):
        listaMusicas = self.listaMusicas
        listaMusicasAlbum = self.listaMusicasAlbum
        self.limiteIns = LimiteCadastraAlbum(self, listaMusicas) 

    def cadastraMusica (self):
        self.limiteMusica = LimiteCadastraMusica(self)

    def consultaAlbum(self):
        self.limiteConsulta = LimiteConsultaAlbum(self)

    def insereMusica(self, event):
        musicaSel = self.limiteIns.listbox.get(tk.ACTIVE)
        musica = self.getMusica(musicaSel)
        self.listaMusicas.append(musica)
        self.limiteIns.mostraJanela('Sucesso', 'Música cadastrada')
        self.limiteIns.listbox.delete(tk.ACTIVE)


    def enterHandler(self, event):
        Artista = self.limiteIns.inputArtista.get()
        Titulo = self.limiteIns.inputTitulo.get()
        Ano = self.limiteIns.inputAno.get()
        
        album = Album(Titulo, Artista, Ano, self.listaMusicasAlbum)
        self.listaAlbuns.append(Album)
        self.limiteIns.mostraJanela('Sucesso', 'Album cadastrado com sucesso')
        self.clearHandler(event)

    def enterMusicHandler(self, event):
        Musica = self.limiteMusica.inputNome.get()
        self.listaMusicasAlbum.append(Musica)
        self.limiteMusica.mostraJanela('Sucesso', 'Música cadastrada com sucesso')
        self.clearHandler(event)

    def consultHandler (self, event):
        str = ''
        Titulo = self.limiteConsulta.inputTitulo.get()
        for nome in self.listaAlbuns:
            if Titulo == nome.titulo:
                str += 'Título do Album: ' + Titulo + '\n'
                str += 'Músicas: ' + '\n'
                for msc in self.listaMusicasAlbum:
                    str += msc + '\n'
        self.limiteConsulta.mostraJanela('Consulta', str)



    def clearHandler(self, event):
        self.limiteIns.inputArtista.delete(0, len(self.limiteIns.inputArtista.get()))
        self.limiteIns.inputTitulo.delete(0, len(self.limiteIns.inputTitulo.get()))
        self.limiteIns.inputAno.delete(0, len(self.limiteIns.inputAno.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()