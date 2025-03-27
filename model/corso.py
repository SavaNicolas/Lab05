class Corso:
    def __init__(self, codins, crediti, nome):
        self.codins = codins #codice corso222
        self.crediti = crediti
        self.nome = nome

    def __str__(self):
        return f' {self.nome} ({self.codins})'