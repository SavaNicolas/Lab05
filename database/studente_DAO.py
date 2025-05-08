# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import DBconnect
import mysql.connector
from model.studente import Studente

class StudenteDAO:
    def get_studenti(self):
        """
        ti restituisce la lista di studenti che è nel database
        :return: lista di studenti
        """
#connessione
        cnx= DBconnect.get_connection()
#cursor
        cursor= cnx.cursor(dictionary=True)
        query = "SELECT * FROM studente"
        cursor.execute(query)
#operazioni
        risultato = []
        for studente in cursor:
            risultato.append(Studente(studente["matricola"],studente["cognome"],studente["nome"],studente["CDS"],studente["corsi"]))

        cursor.close()
        cnx.close()
        return risultato

    def get_iscrittiCorso(codins):
        """
        studente ha matricola
        iscrizione ha matricola e codins

        la query mi deve prendere studente che ha la matricola associata a quel codins
        :return:
        """
        # connessione
        cnx = DBconnect.get_connection()
        # cursor
        cursor = cnx.cursor(dictionary=True)
        query = ("SELECT studente.* FROM iscrizione,studente WHERE iscrizione.matricola = studente.matricola AND iscrizione.codins=%s")
        cursor.execute(query, (codins,))
        # operazioni
        risultato = []
        for studente in cursor:
            risultato.append(Studente(studente["matricola"], studente["cognome"], studente["nome"], studente["CDS"]))

        cursor.close()
        cnx.close()
        return risultato

    def cercaNome(matricola):
        """
        restituisci nome e cognome inerenti alla matricola passata come parametro
        """
        # connessione
        cnx = DBconnect.get_connection()
        # cursor
        cursor = cnx.cursor(dictionary=True)
        query = (
            "SELECT studente.nome, studente.cognome FROM studente WHERE studente.matricola=%s")
        cursor.execute(query, (int(matricola),))

        # Lettura del risultato
        risultato = None
        for row in cursor:  # Iteriamo come in get_iscrittiCorso
            risultato = row  # Dato che ci aspettiamo un solo risultato, sovrascriviamo

        cursor.close()
        cnx.close()
        return risultato if risultato else {}  # Ritorna dizionario vuoto se nulla trovato

