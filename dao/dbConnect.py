import mysql.connector

class DBConnect:

    #UTILIZZANDO IL CLASS METHOD NON POSSO ANDARE A CREARE DIVERSE ISTANZE PER LA CONNESSIONE
    @classmethod
    def getConnection(cls):

        try:
            cnx =  mysql.connector.connect(
                user='root',
                password='',
                host='127.0.0.1',
                database='sw_gestionale'
            )
            return cnx
        except mysql.connector.Error as err:
            print("non riesco a collegarmi al DB")
            print(err)
            return None