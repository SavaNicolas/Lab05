from database.corso_DAO import CorsoDAO
from model.corso import Corso
from model.studente import Studente
from database.studente_DAO import StudenteDAO

class Model:

    def restituisciStudenti(self,corso):
        """
        prende in ingresso l'oggetto corso
        :param corso:
        :return:
        """
        return StudenteDAO.get_iscrittiCorso(corso)

    def cercaNomeda(self,matricola):
        """
        prende in ingresso la matricola e restituisce il nome e il cognome
        :param matricola:
        :return:
        """
        return StudenteDAO.cercaNome(matricola) #è un dizionario

    def cercaCorsi(self,matricola):
        return CorsoDAO.get_corsiStudente(matricola)