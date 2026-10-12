class Strumento:
    def __init__(self,id_strumento,tipo, marca, anno_acquisto, valore):
        self.id_strumento = id_strumento
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = anno_acquisto
        self.valore = valore

    def __str__(self):
        return f"{self.id_strumento},{self.tipo},{self.marca},{self.anno_acquisto},{self.valore}"

    def __repr__(self):
        return f"Strumento: {self.id_strumento},{self.tipo},{self.marca},{self.anno_acquisto}"

