# Add whatever it is needed to interface with the DB Table corso
#query per scegliere i corsi e poi crearli con la classe che c'è in model

from database.DB_connect import DBconnect
import mysql.connector
from model.corso import Corso
from model.studente import Studente


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

    def get_corsiStudente(matricola):
        """

                la query mi deve prendere i corsi associati a quella matricola
                :return: lista di studenti
                """
        # connessione
        cnx = DBconnect.get_connection()
        # cursor
        cursor = cnx.cursor(dictionary=True)
        query = ( "SELECT corso.* FROM corso, iscrizione WHERE iscrizione.codins=corso.codins AND iscrizione.matricola=%s")
        cursor.execute(query, (matricola,))
        # operazioni
        risultato = []
        counter=0
        for corso in cursor:
            risultato.append(Corso(corso["codins"], corso["crediti"], corso["nome"]))
            counter+=1

        cursor.close()
        cnx.close()
        return risultato,counter