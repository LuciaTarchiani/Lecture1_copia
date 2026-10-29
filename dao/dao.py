import mysql.connector

from dao.dbConnect import DBConnect
from gestionale.core.cliente import ClienteRecord
from gestionale.core.prodotto import ProdottoRecord


#le classi dao contentgono tutti e soli i metodi che fanno le queries al database

# generalmente abbiamo una classe dao per ogni database con cui vogliamo interagire
# noi solitamente avremo una sola classe perchè interagiamo con un solo database

class DAO:

    def getAllProdotti(self):

        #cnx = mysql.connector.connect(
            #user = "root",
            #password = "",
            #host = "127.0.0.1",
            #database = "sw_gestionale"
        #)
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary=True)
        #generalemente noi andiamo a testare le query su DBeaver e, dopo averla testata,
        # andiamo ad incollare la query all'interno di execute()
        cursor.execute("SELECT * FROM prodotti")
        #dopo aver eseguito la query dobbiamo andare a recuperare i dati del result set
        row = cursor.fetchall()

        #CREIAMO DEGLI OGGETTI DI TIPO PRODOTTO
        res = []
        #cicliamo sulla tabella che abbiamo ricevuto come result set
        for p in row:
            """NOME E PREZZO SONO I NOMI PRESTENTI NEL DATABASE"""
            res.append(ProdottoRecord(p["nome"],p["prezzo"]))

        cursor.close()
        cnx.close()
        return res

    def getAllClienti(self):
        cnx = mysql.connector.connect(
            user = "root",
            password = "",
            host = "127.0.0.1",
            database = "sw_gestionale"
        )

        cursor = cnx.cursor(dictionary=True)
        #generalemente noi andiamo a testare le query su DBeaver e, dopo averla testata,
        # andiamo ad incollare la query all'interno di execute()
        cursor.execute("SELECT * FROM clienti")
        #dopo aver eseguito la query dobbiamo andare a recuperare i dati del result set
        row = cursor.fetchall()

        #CREIAMO DEGLI OGGETTI DI TIPO PRODOTTO
        res = []
        #cicliamo sulla tabella che abbiamo ricevuto come result set
        for p in row:
            """NOME E PREZZO SONO I NOMI PRESTENTI NEL DATABASE"""
            res.append(ClienteRecord(p["nome"],p["mail"],p["categoria"]))

        cursor.close()
        cnx.close()
        return res

    def addProdotto(self,prodotto):
        cnx = mysql.connector.connect(
            user="root",
            password="",
            host="127.0.0.1",
            database="sw_gestionale"
        )

        cursor = cnx.cursor()
        cursor.execute("""insert into prodotti 
                        (nome,prezzo) values (%s,%s)""", (prodotto.name,prodotto.prezzo_unitario))
        cnx.commit()
        cursor.close()
        cnx.close()
        return

    def addCliente(self,cliente):
        cnx = mysql.connector.connect(
            user="root",
            password="",
            host="127.0.0.1",
            database="sw_gestionale"
        )

        cursor = cnx.cursor()
        cursor.execute("""insert into clienti 
                        (nome,mail,categoria) values (%s,%s,%s)""",
                       (cliente.nome,cliente.mail, cliente.categoria))
        cnx.commit()
        cursor.close()
        cnx.close()
        return

    def hasCliente(self,cliente):
        cnx = mysql.connector.connect(
            user = "root",
            password = "",
            host = "127.0.0.1",
            database = "sw_gestionale"
        )

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clienti where mail = %s", (cliente.mail,))
        row = cursor.fetchall()

        cursor.close()
        cnx.close()
        return len(row) > 0

    def hasProdotto(self, prod):
        cnx = mysql.connector.connect(
            user="root",
            password="",
            host="127.0.0.1",
            database="sw_gestionale"
        )

        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM prodotti where nome = %s", (prod.name,))
        row = cursor.fetchall()

        cursor.close()
        cnx.close()
        return len(row) > 0


if __name__ == "__main__":
    myDao = DAO()
    myDao.getAllProdotti()