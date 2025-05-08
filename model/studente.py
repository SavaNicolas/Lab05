class Studente:
    def __init__(self, matricola,cognome,nome,CDS):
        self.matricola = matricola #chiave
        self.cognome = cognome
        self.nome = nome
        self.CDS = CDS #corso di studi
        self.corsi= [] #ogni studente può frequentare più corsi

    def __str__(self):
        return f"{self.nome}, {self.cognome} ({self.matricola})"
    def __eq__(self, other):
        pass
    def __hash__(self):
        pass