import tkinter as tk
from tkinter import messagebox
import artista as ast
import album as alb
import playlist as play

#2022004251 - João Vítor Botrel

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)
        self.artistaMenu = tk.Menu(self.menubar)
        self.albumMenu = tk.Menu(self.menubar)
        self.playlistMenu = tk.Menu(self.menubar)


        self.artistaMenu.add_command(label="Cadastra", command=self.controle.cadastraArtista)
        self.artistaMenu.add_command(label="Consulta", command=self.controle.consultaArtista)
        self.menubar.add_cascade(label="Artista", menu=self.artistaMenu)

        
        self.albumMenu.add_command(label="Cadastrar música", command=self.controle.cadastraMusica)
        self.albumMenu.add_command(label="Cadastrar",
                                    command=self.controle.cadastraAlbum)
        self.albumMenu.add_command(label="Consulta",
                                    command=self.controle.consultaAlbum)
        self.menubar.add_cascade(label="Album", menu=self.albumMenu)


        self.playlistMenu.add_command(label="Cadastrar", command=self.controle.cadastraPlaylist)
        self.playlistMenu.add_command(label="Consultar", command=self.controle.consultaPlaylist)
        self.menubar.add_cascade(label="Playlist", menu=self.playlistMenu)

        self.root.config(menu=self.menubar)


class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlArtista = ast.CtrlArtista(self)
        self.ctrlAlbum = alb.CtrlAlbum()
        self.ctrlPlaylist = play.CtrlPlaylist(self)

        self.limite = LimitePrincipal(self.root, self)

        self.root.title("Spotify")
        # Inicia o mainloop
        self.root.mainloop()

    def cadastraArtista(self):
        self.ctrlArtista.cadastraArtista()

    def consultaArtista(self):
        self.ctrlArtista.consultaArtista()

    def cadastraAlbum(self):
        self.ctrlAlbum.cadastraAlbum()

    def cadastraMusica(self):
        self.ctrlAlbum.cadastraMusica()

    def consultaAlbum(self):
        self.ctrlAlbum.consultaAlbum()

    def cadastraPlaylist(self):
        self.ctrlPlaylist.cadastraPlaylist()

    def consultaPlaylist(self):
        self.ctrlPlaylist.consultaPlaylist()


if __name__ == '__main__':
    c = ControlePrincipal()