class Prestito:
    def __init__(self,id_prestito,data, id_strumento, cognome_allievo):
        self.id_prestito = id_prestito
        self.data = data
        self.id_strumento = id_strumento
        self.cognome_allievo = cognome_allievo

    def __str__(self):
        return f"Prestito {self.id_prestito}: Strumento {self.id_strumento} affidato a {self.cognome_allievo} in data {self.data}"

    def __repr__(self):
        return f"Prestito: {self.id_prestito},{self.data},{self.id_strumento},{self.cognome_allievo}"


