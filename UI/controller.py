import flet as ft

from database.corso_DAO import CorsoDAO
from model import corso
from database import corso_DAO as c



class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_cercaStudenti(self, e):
        """ cerca studenti, se lo trova mi riempe nome e cognome a dx"""
        matricola= self._view.txt_matricola.value

        if matricola is None or matricola == "":
            self._view.create_alert("Inserire la matricola")
            return

        dict_nomeCognome= self._model.cercaNomeda(matricola) #potrebbe essere vuoto {}

        if not dict_nomeCognome:
            self._view.create_alert("matricola non trovata")
            return

        self._view.txt_nome.value= f"{dict_nomeCognome["nome"]}"
        self._view.txt_cognome.value= f"{dict_nomeCognome["cognome"]}"
        self._view.update_page()

    def handle_cercaCorsi(self, e):
        """
        inserisco la matricola e mi da i corsi a cui è iscritto
        :param e:
        :return:
        """
        matricola=self._view.txt_matricola.value
        if matricola is None or matricola == "":
            self._view.create_alert("Inserire la matricola")
            return
        corsi,counter= self._model.cercaCorsi(matricola)
        self._view.txt_result.controls.append(ft.Text(f"Lo studente è iscritto a {counter} corsi:"))
        for corso in corsi:
            self._view.txt_result.controls.append(ft.Text(f"{corso.__str__()}"))

        self._view.update_page()

    def handle_iscrivi(self, e):
        pass

    def handle_cercaIscritti(self,e):
        """
        metodo che ti restituisce gli iscritti al corso selezionato.
        se non viene selezionato nessun corso avvisa l'utente con un allert dialog
        :param e:
        :return:
        """
        corsoSelezionato= self._view._selezionaCorso.value
        if corsoSelezionato is None or corsoSelezionato == "":
            self._view.create_alert("Selezionare il corso")
            return

        #se non entra restituisci studenti iscritti a quel corso
        studentiCorso= self._model.restituisciStudenti(corsoSelezionato)#array studenti
        for studente in studentiCorso:
            self._view.txt_result.controls.append(ft.Text(studente.__str__()))

        self._view.update_page()




    def fillCorso(self):
        dao = CorsoDAO()
        corsi=dao.get_corsi()
        for corso in corsi:
            self._view._selezionaCorso.options.append( ft.dropdown.Option (key=corso.codins, text=corso.__str__()))
        self._view.update_page()


