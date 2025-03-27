# Add whatever it is needed to interface with the DB Table corso
#query per scegliere i corsi e poi crearli con la classe che c'è in model

from database.DB_connect import DBconnect
import mysql.connector
from model.corso import Corso
class CorsoDAO:
    def get_corsi(self):
        """
        ti restituisce la lista di corsi che è nel database
        :return: lista di corsi
        """
#connessione
        cnx= DBconnect.get_connection()
#cursor
        cursor= cnx.cursor(dictionary=True)
        query = "SELECT * FROM corso"
        cursor.execute(query)
#operazioni
        risultato = []
        for corso in cursor:
            risultato.append(Corso(corso["codins"],corso["crediti"],corso["nome"]))

        cursor.close()
        cnx.close()
        return risultato


