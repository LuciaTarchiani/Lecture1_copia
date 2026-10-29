import flet as ft

from gestionale.gestoreOrdini import GestoreOrdini


class Controller:
    def __init__(self,view):
        self._view = view
        self._model = GestoreOrdini()

    """
    TUTTE LE FUNZIONI ASSOCIATE AD UN BOTTONE DEVONO PRENDERE IN INPUT L'EVENTO 
    """
    def add_ordine(self,e):
        #legge i campi di testo e aggiunge un ordine
        #PRODOTTO
        nomePstr = self._view._txtInNomeP.value
        if nomePstr == "":
            self._view._lvOut.controls.append(ft.Text("attenzione il campo nome prodotto NON può essre vuoto", color = "red"))
            self._view.update_page()
            return
        try:
            prezzo= float(self._view._txtInPrezzo.value)
        except ValueError:
            #vado a scrivere nella list view che l'utente ha sbagliato
            self._view._lvOut.controls.append(
                ft.Text("Attenzione il prezzo deve esser un numero", color = "red")
            )
            self._view.update_page()
            return

        try:
            quantita = int(self._view._txtInQuantita.value)
        except ValueError:
            # vado a scrivere nella list view che l'utente ha sbagliato
            self._view._lvOut.controls.append(
                ft.Text("Attenzione la quantita deve esser un numero", color="red")
            )
            self._view.update_page()
            return


        #CLIENTE
        nomeCstr = self._view._txtInNomeC.value
        if nomeCstr== "":
            self._view._lvOut.controls.append(ft.Text("attenzione il campo nome cliente NON può essre vuoto", color = "red"))
            self._view.update_page()
            return
        mailstr = (self._view._txtInMail.value)
        if mailstr == "":
            self._view._lvOut.controls.append(ft.Text("attenzione il campo mail NON può essre vuoto", color = "red"))
            self._view.update_page()
            return
        categoriastr = self._view._txtInCategoria.value
        if categoriastr == "":
            self._view._lvOut.controls.append(ft.Text("attenzione il campo categoria NON può essre vuoto", color = "red"))
            self._view.update_page()
            return

        #POSSO ADESSO CREARE UN NUOVO ORDINE- CHIAMO IL METODO DEL MIO GESTORE
        ordine = self._model.crea_ordine(nomePstr,prezzo,quantita,nomeCstr,mailstr,categoriastr)
        self._model.add_ordine(ordine)
        # dopo aver creato l'ordine è buona norma andare a pulire l'interfaccia grafica
        self._view._txtInNomeP.value = ""
        self._view._txtInPrezzo.value = ""
        self._view._txtInQuantita.value = ""
        self._view._txtInNomeC.value = ""
        self._view._txtInMail.value = ""
        self._view._txtInCategoria.value = ""

        self._view._lvOut.controls.append(
            ft.Text("Ordine aggiunto con successo", color = "green")
        )
        self._view._lvOut.controls.append(
            ft.Text("dettagli dell'ordine")
        )
        self._view._lvOut.controls.append(
            ft.Text(ordine.riepilogo())
        )
        self._view.update_page()


    def gestisci_ordine(self,e):
        #andiamo a pulire il list view
        self._view._lvOut.controls.clear()
        res, ordine = self._model.processa_prossimo_ordine()
        # il metodo processa_prossimo_ordine fa return false se non ci sono altri oridini in coda
        #mentre fa retrun true se viene gestito correttamente
        if res:
            self._view._lvOut.controls.append(
                ft.Text("Ordine processato correttamente", color = "green")
            )
            self._view._lvOut.controls.append(
                #stampo l'ordine gestito
                ft.Text(ordine.riepilogo())
            )
            self._view.update_page()
        else:
            self._view._lvOut.controls.append(
                ft.Text("non ci sono ordini in coda", color ="blue")
            )
            self._view.update_page()

    def gestisci_all_ordini(self,e):
        self._view._lvOut.controls.clear()
        ordini = self._model.processa_tutti_ordini()
        if not ordini:
            self._view._lvOut.controls.append(
                ft.Text("NON ci sono ordini in coda", color = "blue")
            )
            self._view.update_page()
        else:

            self._view._lvOut.controls.append(
                ft.Text(f"ho processatto correttamente {len(ordini)} ordini", color = "green")
            )
            for o in ordini:
                self._view._lvOut.controls.append(ft.Text("\n"))
                self._view._lvOut.controls.append(
                    ft.Text(o.riepilogo())
                )
            self._view.update_page()

    def stampa_sommario(self,e):
        self._view._lvOut.controls.clear()
        self._view._lvOut.controls.append(
            ft.Text("Di seguito il sommario dello stato del business", color = "orange")
        )
        self._view._lvOut.controls.append(
            ft.Text(self._model.get_riepilogo())
        )
        self._view.update_page()