from dataclasses import dataclass

@dataclass
class ClienteRecord:
    nome: str
    mail: str
    categoria: str

#queste dataclass devono avere alcune funzioni:

    def __hash__(self):
    #la chiave primaria è la mail
    #se due istanze della classe clienteRecord hanno lo stesso valore per il campo mail
    #allora sono lo stesso oggetto
        return hash(self.mail)

    def __eq__(self,other):
        #USIAMO LA CHIAVE PRIMARIA DEL DATABASE PER STABILIRE SE DUE OGGETTI SONO IDENTICI
        self.mail == other.mail

    def __str__(self):
        return f"{self.nome} -- {self.mail} ({self.categoria})"