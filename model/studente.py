class Studente:
    def __init__(self, matricola,nome,cognome, corsi):
        self.matricola = matricola #chiave
        self.nome = nome
        self.cognome = cognome
        self.corsi= [] #ogni studente può frequentare più corsi

