from Domain.rezervare import to_string
from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare
from Logic.functionality import trece_clasa_superioara


def print_menu():
    print("1. Adaugare rezervare")
    print("2. Stergere rezervare")
    print("3. Modificare rezervare")
    print("a. Afisare rezervari")
    print("4. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară")
    print("x. Iesire")


def ui_adauga_rezervare(lista):
    try:
        ID = input("Dati ID-ul: ")
        nume = input("Dati numele: ")
        clasa = input("Dati clasa (economy, economy plus, business): ")
        pret = float(input("Dati pretul: "))
        checkin_facut = input("Dati checkin_facut-ul (da / nu):")
        return adauga_rezervare(ID, nume, clasa, pret, checkin_facut, lista)
    except ValueError as ve:
        print("Eroare: ", ve)
        return lista


def ui_sterge_rezervare(lista):
    try:
        ID = input("Dati ID-ul rezervarii care trebuie stearsa: ")
        return sterge_rezervare(ID, lista)
    except ValueError as ve:
        print("Eroare: ", ve)
        return lista


def ui_modifica_rezervare(lista):
    try:
        ID = input("Dati ID-ul rezervarii care trebuie modificata: ")
        nume = input("Dati noul nume: ")
        clasa = input("Dati noua clasa (economy, economy plus, business): ")
        pret = input("Dati noul pret: ")
        checkin_facut = input("Dati noul checkin_facut (da / nu):")
        return modifica_rezervare(ID, nume, clasa, pret, checkin_facut, lista)
    except ValueError as ve:
        print("Eroare: ", ve)
        return lista


def show_all(lista):
    for rezervare in lista:
        print(to_string(rezervare))


def ui_trece_clasa_superioara(lista):
    nume = input("Dati numele: ")
    return trece_clasa_superioara(lista, nume)


def run_menu(lista):
    while True:
        print_menu()
        optiune = input("Dati optiune: ")
        if optiune == "1":
            lista = ui_adauga_rezervare(lista)
        elif optiune == "2":
            lista = ui_sterge_rezervare(lista)
        elif optiune == "3":
            lista = ui_modifica_rezervare(lista)
        elif optiune == "a":
            show_all(lista)
        elif optiune == "4":
            lista = ui_trece_clasa_superioara(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
