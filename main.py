from deposito_strumenti import DepositoStrumenti
from datetime import datetime

def menu():
    print("\n--- MENU DEPOSITO STRUMENTI ---")
    print("1. Modifica nome del responsabile del deposito")
    print("2. Carica strumenti da file")
    print("3. Aggiungi un nuovo strumento (da tastiera)")
    print("4. Visualizza strumenti ordinati per marca")
    print("5. Presta uno strumento")
    print("6. Termina prestito strumento")
    print("7. Esci")
    return input("Scegli un'opzione >> ")

def main():
    deposito = DepositoStrumenti("Deposito Strumenti Civico", "Alessandro Visconti")

    while True:
        scelta = menu()

        if scelta == "1":
            nuovo_responsabile = input("Inserisci il nuovo responsabile: ")
            # TODO: Aggiorna responsabile nel sistema
            deposito.responsabile = nuovo_responsabile
            print("Responsabile aggiorato")

        elif scelta == "2":
            while True:
                try:
                    file_path = input("Inserisci il path del file da caricare: ").strip()
                    deposito.carica_file_strumenti(file_path)
                    break
                except Exception as e:
                    print(e)

        elif scelta == "3":
            tipo = input("Tipo di strumento: ")
            marca = input("Marca: ")
            try:
                anno_acquisto = int(input("Anno di acquisto: ").strip())
                valore = float(input("Valore (euro): ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno e valore.")
                continue
            strumento = deposito.aggiungi_strumento(tipo, marca, anno_acquisto, valore)
            print(f"Strumento aggiunto: {strumento}")

        elif scelta == "4":
            strumenti_ordinati = deposito.strumenti_ordinati_per_marca()
            for s in strumenti_ordinati:
                print(f'- {s}')

        elif scelta == "5":
            id_strumento = input("ID strumento: ")
            cognome_allievo = input("Cognome allievo: ")
            data = datetime.now().date()
            try:
                prestito = deposito.nuovo_prestito(data, id_strumento, cognome_allievo)
                print(f"Prestito andato a buon fine: {prestito}")
            except Exception as e:
                print(e)

        elif scelta == "6":
            id_prestito = input("ID prestito da terminare: ")
            try:
                deposito.termina_prestito(id_prestito)
                print(f"Prestito {id_prestito} terminato con successo.")
            except Exception as e:
                print(e)

        elif scelta == "7":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida!")

if __name__ == "__main__":
    main()
