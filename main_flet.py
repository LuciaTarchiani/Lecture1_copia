import flet as ft

from UI.controller import Controller
from UI.view import View

#deve far comunicare il controller con la view e con il gestore ordini

"""
nella funzione main creiamo un oggetto di tipo view, un oggetto di tipo controller
e li facciamo parlare 
"""

def main(page: ft.Page):
    v = View(page) #creo il view da solo e gli passo la pagina dove caricare l'interfaccia
    c = Controller(v) #vado a dire al controller qual è il mio view
    v.set_controller(c)# vado ad implementare un metodo dentro view per informarlo di qual è il suo controller
    v.carica_interfaccia()


"""
chiamata al metodo app di flet che ha come argomento la funzione che regola il comportamento
della nostra applicazione grafica (ovvero la funzione main scritta sopra)
"""
ft.app(target = main)