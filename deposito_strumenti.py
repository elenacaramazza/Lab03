from strumento import Strumento
from prestito import Prestito
from operator import attrgetter

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome=nome
        self.responsabile=responsabile
        self.strumenti={} #Dizionario: id_strumento -> Strumento
        self.prestiti={} #Dizionario: id_prestito -> Prestito
        self.strumenti_in_prestito = set() # Insieme con gli ID degli strumenti attualmente in prestito

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            file=open(file_path, "r")
            for line in file:
                line=line.strip().split(",")
                id_strumento=line[0]
                tipo=line[1]
                marca=line[2]
                anno_acquisto=line[3]
                valore=line[4]

                self.strumenti[id_strumento]=Strumento(id_strumento, tipo, marca, anno_acquisto, valore)
            file.close()

        except FileNotFoundError:
            raise FileNotFoundError(f"File non trovato")

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        num=len(self.strumenti)+1
        id_strumento=f"S{num}"
        strumento=Strumento(id_strumento,tipo, marca, anno_acquisto, valore)
        self.strumenti[id_strumento]=strumento
        return strumento

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        return sorted(self.strumenti.values(), key=attrgetter('marca'))

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        if id_strumento not in self.strumenti:
            raise Exception(f"Lo strumento {id_strumento} non esiste nel deposito")
        if id_strumento in self.strumenti_in_prestito:
            raise Exception(f"Lo strumento {id_strumento} è già in prestito")

        num=len(self.prestiti)+1
        id_prestito=f"P{num}"
        prestito=Prestito(id_prestito,data, id_strumento, cognome_allievo)
        self.prestiti[id_prestito]=prestito
        self.strumenti_in_prestito.add(id_strumento)
        return prestito

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        if id_prestito not in self.prestiti:
            raise Exception(f"Il prestito {id_prestito} non esiste nel deposito")

        prestito=self.prestiti.pop(id_prestito)
        self.strumenti_in_prestito.remove(prestito.id_strumento)
