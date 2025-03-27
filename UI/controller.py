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
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def handle_cercaCorsi(self, e):
        pass

    def handle_iscrivi(self, e):
        pass

    def handle_cercaIscritti(self,e):
        pass

    def fillCorso(self):
        dao = CorsoDAO()
        corsi=dao.get_corsi()
        for corso in corsi:
            self._view._selezionaCorso.options.append( ft.dropdown.Option (key=corso.codins, text=corso.__str__()))
        self._view.update_page()


