from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare
from Logic.functionality import trece_clasa_superioara, ieftinire
from UserInterface.console import ui_pret_max_clasa, ui_ordonare_descrescator_pret, ui_suma_pret, show_all


def print_menu_2():
    print("help: Afisare meniu")
    print("add: Adaugare rezervare")
    print("delete: Stergere rezervare")
    print("modify: Modificare rezervare")
    print("show: Afisare rezervari")
    print("3.2: Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară")
    print("3.3: Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit")
    print("3.4: Determinarea prețului maxim pentru fiecare clasă.")
    print("3.5: Ordonarea rezervărilor descrescător după preț.")
    print("3.6:  Afișarea sumelor prețurilor pentru fiecare nume.")
    print("undo: Undo")
    print("stop: Iesire")


def ui_adauga_rezervare_2(ID, nume, clasa, pret, checkin_facut, lista, undo_list):
    try:
        rezultat = adauga_rezervare(ID, nume, clasa, pret, checkin_facut, lista)
        undo_list.append(lista)
        return rezultat
    except ValueError as ve:
        print("Eroare: ", ve)
        return lista


def ui_sterge_rezervare_2(ID, lista, undo_list):
    try:
        rezultat = sterge_rezervare(ID, lista)
        undo_list.append(lista)
        return rezultat
    except ValueError as ve:
        print("Eroare: ", ve)
        return lista


def ui_modifica_rezervare_2(ID, nume, clasa, pret, checkin_facut, lista, undo_list):
    try:
        rezultat = modifica_rezervare(ID, nume, clasa, pret, checkin_facut, lista)
        undo_list.append(lista)
        return rezultat
    except ValueError as ve:
        print("Eroare: ", ve)
        return lista


def ui_trece_clasa_superioara_2(lista, nume, undo_list):
    undo_list.append(lista)
    return trece_clasa_superioara(lista, nume)


def ui_ieftinire_2(lista, procentaj, undo_list):
    try:
        rezultat = ieftinire(lista, procentaj)
        undo_list.append(lista)
        return rezultat
    except ValueError as ve:
        print("Eroare! ", ve)


def run_menu_2(lista):
    undo_list = []
    while True:
        cerinta = input("Dati cerinta: ")
        if cerinta == "stop":
            break
        else:
            lista_cerinte = cerinta.split(";")
            for c in lista_cerinte:
                if c == "help":
                    print_menu_2()
                elif c[0:3] == "add":
                    ID = c.split(",")[1]
                    nume = c.split(",")[2]
                    clasa = c.split(",")[3]
                    pret = float(c.split(",")[4])
                    checkin_facut = c.split(",")[5]
                    lista = ui_adauga_rezervare_2(ID, nume, clasa, pret, checkin_facut, lista, undo_list)
                elif c[0:4] == "show":
                    show_all(lista)
                elif c[0:6] == "delete":
                    ID = c.split(",")[1]
                    lista = ui_sterge_rezervare_2(ID, lista, undo_list)
                elif c[0:6] == "modify":
                    ID = c.split(",")[1]
                    nume = c.split(",")[2]
                    clasa = c.split(",")[3]
                    pret = c.split(",")[4]
                    checkin_facut = c.split(",")[5]
                    lista = ui_modifica_rezervare_2(ID, nume, clasa, pret, checkin_facut, lista, undo_list)
                elif c[0:3] == "3.2":
                    nume = c.split(",")[1]
                    lista = ui_trece_clasa_superioara_2(lista, nume, undo_list)
                elif c[0:3] == "3.3":
                    procentaj = float(c.split(",")[1])
                    lista = ui_ieftinire_2(lista, procentaj, undo_list)
                elif c[0:3] == "3.4":
                    ui_pret_max_clasa(lista)
                elif c[0:3] == "3.5":
                    lista = ui_ordonare_descrescator_pret(lista, undo_list)
                elif c[0:3] == "3.6":
                    ui_suma_pret(lista)
                elif c[0:4] == "undo":
                    if len(undo_list) > 0:
                        lista = undo_list.pop()
                    else:
                        print("Nu se poate face Undo")
                else:
                    print("Cerinta inexistenta! Mai incercati")
