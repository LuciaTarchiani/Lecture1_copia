import flet as ft
class View:
    def __init__(self,page):
        self._page = page
        self._controller = None
        self._page.title = "Software Gestionale"
        self._page.horizontal_alignment = ft.MainAxisAlignment.CENTER
        self.update_page()

        #teoricamente nel costruttore dovre iniziallizzare tuttu gli oggetti grafici
        # che abbiamo creato nella nostra funzione carcia_interfaccia, quindi:
        self._txtInNomeP = None
        """L'INIZIALIZZAZIONE DELLE VARIE ISTANZE IN PYTHON NON è OBBLIGATORIO FARLO NEL COSTRUTTORE, 
        IL PYTHON POSSIAMO CREARE PROPRIETA' DI UNA CLASSE DOVE VOGLIAMO [in java era obbligatorio farlo nel costruttore]"""

    def carica_interfaccia(self):

        #PRODOTTO - ha 3 campi di testo
        self._txtInNomeP = ft.TextField(label="Nome Prodotto", width=200) #att: value è il valore effettivamente inserito dall'utente
        self._txtInPrezzo = ft.TextField(label="Prezzo", width=200)
        self._txtInQuantita= ft.TextField(label="Quantità", width=200)

        row1 = ft.Row([self._txtInNomeP,self._txtInPrezzo, self._txtInQuantita],
                      alignment=ft.MainAxisAlignment.CENTER)


        #CLIENTE
        self._txtInNomeC = ft.TextField(label = "Nome Cliente", width=200)
        self._txtInMail = ft.TextField(label="E-mail", width=200)
        self._txtInCategoria = ft.TextField(label="Categoria", width=200)

        row2 = ft.Row([self._txtInNomeC,self._txtInMail,self._txtInCategoria],
                      alignment=ft.MainAxisAlignment.CENTER)

        #BUTTONS
        self._btnAdd = ft.ElevatedButton("Aggiungi Ordine",
                                         on_click= self._controller.add_ordine,
                                         #ATT: IL METODO ASSOCIATO è SCRITTO NEL CONTROLLER,
                                         #NON POSSO PASSARE DIRETTAMENTE UN METODO DEL MAIN
                                         width=200)
        self._btnGestisciOrdine = ft.ElevatedButton("Gestisci prox ordine",
                                                    on_click= self._controller.gestisci_ordine,
                                                    width=200)
        self._btnGestisciAllOrdini = ft.ElevatedButton("Gestisci tutti gli ordini",
                                                    on_click= self._controller.gestisci_all_ordini,
                                                    width=200)
        self._btnStampaInfo = ft.ElevatedButton("Stampa sommario",
                                                    on_click= self._controller.stampa_sommario,
                                                    width=200)

        row3 = ft.Row([self._btnAdd, self._btnGestisciOrdine,self._btnGestisciAllOrdini,self._btnStampaInfo],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._lvOut = ft.ListView(expand = True)

        self._page.add(row1,row2,row3,self._lvOut)


    def set_controller(self,c):
        self._controller = c

    def update_page(self):
        self._page.update()


