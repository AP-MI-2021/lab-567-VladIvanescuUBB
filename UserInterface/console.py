from copy import deepcopy

from Domain.rezervare import to_string, get_nume
from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare
from Logic.functionality import trece_clasa_superioara, ieftinire, pret_max_clasa, ordonare_descrescator_pret, suma_pret


def print_menu():
    print("1. Adaugare rezervare")
    print("2. Stergere rezervare")
    print("3. Modificare rezervare")
    print("a. Afisare rezervari")
    print("4. Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară")
    print("5. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit")
    print("6. Determinarea prețului maxim pentru fiecare clasă.")
    print("7. Ordonarea rezervărilor descrescător după preț.")
    print("8.  Afișarea sumelor prețurilor pentru fiecare nume.")
    print("u. Undo")
    print("r. Redo")
    print("x. Iesire")


def ui_adauga_rezervare(lista, undo_list, redo_list):
    try:
        ID = input("Dati ID-ul: ")
        nume = input("Dati numele: ")
        clasa = input("Dati clasa (economy, economy plus, business): ")
        pret = float(input("Dati pretul: "))
        checkin_facut = input("Dati checkin_facut-ul (da / nu):")
        rezultat = adauga_rezervare(ID, nume, clasa, pret, checkin_facut, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: ", ve)
        return lista


def ui_sterge_rezervare(lista, undo_list, redo_list):
    try:
        ID = input("Dati ID-ul rezervarii care trebuie stearsa: ")
        rezultat = sterge_rezervare(ID, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: ", ve)
        return lista


def ui_modifica_rezervare(lista, undo_list, redo_list):
    try:
        ID = input("Dati ID-ul rezervarii care trebuie modificata: ")
        nume = input("Dati noul nume: ")
        clasa = input("Dati noua clasa (economy, economy plus, business): ")
        pret = input("Dati noul pret: ")
        checkin_facut = input("Dati noul checkin_facut (da / nu):")
        rezultat = modifica_rezervare(ID, nume, clasa, pret, checkin_facut, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: ", ve)
        return lista


def show_all(lista):
    for rezervare in lista:
        print(to_string(rezervare))


def ui_trece_clasa_superioara(lista, undo_list, redo_list):
    nume = input("Dati numele: ")
    undo_list.append(deepcopy(lista))
    redo_list.clear()
    return trece_clasa_superioara(lista, nume)


def ui_ieftinire(lista, undo_list, redo_list):
    try:
        undo_list.append(deepcopy(lista))
        redo_list.clear()
        procentaj = float(input("Dati procentajul: "))
        rezultat = ieftinire(lista, procentaj)
        return rezultat
    except ValueError as ve:
        print("Eroare! ", ve)


def ui_pret_max_clasa(lista):
    print("economy: ", pret_max_clasa(lista, "economy"))
    print("economy plus: ", pret_max_clasa(lista, "economy plus"))
    print("business: ", pret_max_clasa(lista, "business"))


def ui_ordonare_descrescator_pret(lista, undo_list, redo_list):
    undo_list.append(lista)
    redo_list.clear()
    return ordonare_descrescator_pret(lista)


def ui_suma_pret(lista):
    """
    functia afiseaza suma preturilor pentru fiecare nume din lista
    :param lista: lista de rezervari
    """
    nume_curent = ""
    for rezervare in sorted(lista, key=lambda rez: get_nume(rez)):
        nume = get_nume(rezervare)
        if nume != nume_curent:
            print("{}: {}".format(nume, suma_pret(lista, nume)))
        nume_curent = nume


def undo(undo_list):
    """
    functia aduce programul la pasul anterior
    :param undo_list: lista cu istoricul listei de rezervari
    :return: ultimul element din undo_list
    """
    return undo_list.pop()


def redo(redo_list):
    """
    functia aduce programul la pasul ulterior
    :param redo_list: lista cu istoricul listei de undo
    :return: ultimul element din redo_list
    """
    return redo_list.pop()


def run_menu(lista):
    undo_list = []
    redo_list = []
    while True:
        print_menu()
        optiune = input("Dati optiune: ")
        if optiune == "1":
            lista = ui_adauga_rezervare(lista, undo_list, redo_list)
        elif optiune == "2":
            lista = ui_sterge_rezervare(lista, undo_list, redo_list)
        elif optiune == "3":
            lista = ui_modifica_rezervare(lista, undo_list, redo_list)
        elif optiune == "a":
            show_all(lista)
        elif optiune == "4":
            lista = ui_trece_clasa_superioara(lista, undo_list, redo_list)
        elif optiune == "5":
            lista = ui_ieftinire(lista, undo_list, redo_list)
        elif optiune == "6":
            ui_pret_max_clasa(lista)
        elif optiune == "7":
            lista = ui_ordonare_descrescator_pret(lista, undo_list, redo_list)
        elif optiune == "8":
            ui_suma_pret(lista)
        elif optiune == "u":
            if len(undo_list) > 0:
                redo_list.append(lista)
                lista = undo(undo_list)
            else:
                print("Nu se poate face Undo")
        elif optiune == "r":
            if len(redo_list) > 0:
                undo_list.append(lista)
                lista = redo(redo_list)
            else:
                print("Nu se poate face Redo!")
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
