import flet as ft
from UI.controller import Controller


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #row1: seleziona corso + button seleziona iscritti

        self._selezionaCorso = ft.Dropdown(label="Seleziona un corso", hint_text="corso",
                                              options=[], autofocus=True, width=610)
        self._controller.fillCorso() #per riempire control (fallo dopo aver creato la tendina)

            #option lo devi riempire dal controller
        self.btn_cercaIscritti = ft.ElevatedButton(text="Cerca studente",
                                                   on_click=self._controller.handle_cercaIscritti)
            #definisci on click

        row1 = ft.Row([self._selezionaCorso, self.btn_cercaIscritti])

        #row2: matricola(inserisci matricola), nome, cognome
        self.txt_matricola = ft.TextField(
            label="Matricola",
            width=200,
            hint_text="inserisci la tua matricola"
        )
        self.txt_nome = ft.TextField(
            label="Nome",
            width=200,
            read_only=True
            #appare il nome una volta che ho cliccato cerca studente
        )
        self.txt_cognome = ft.TextField(
            label="Cognome",
            width=200,
            read_only=True
            #appare il nome una volta che ho cliccato cerca studente
        )
        row2 = ft.Row([self.txt_matricola, self.txt_nome, self.txt_cognome])
        #row3: bottoni: cerca studente, cerca corsi, iscrivi
        self.btn_cercaStudenti = ft.ElevatedButton(text="Cerca studente", on_click=self._controller.handle_cercaStudenti)
        self.btn_cercaCorsi = ft.ElevatedButton(text="Cerca corsi", on_click=self._controller.handle_cercaCorsi)
        self.btn_iscrivi = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handle_iscrivi)
            #definisci i metodi on click

        row3 = ft.Row([self.btn_cercaStudenti, self.btn_cercaCorsi, self.btn_iscrivi])
        #row 4: lista
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

        #aggiungi tutto
        self._page.add(row1, row2, row3, self.txt_result)
        self._page.update()
    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()





