from Domain.rezervare import to_string
from Logic.CRUD import adauga_rezervare, sterge_rezervare, modifica_rezervare


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
    print("stop: Iesire")


def ui_adauga_rezervare_2(ID, nume, clasa, pret, checkin_facut, lista):
    return adauga_rezervare(ID, nume, clasa, pret, checkin_facut, lista)


def show_all_2(lista):
    for rezervare in lista:
        print(to_string(rezervare))


def ui_sterge_rezervare_2(ID, lista):
    try:
        return sterge_rezervare(ID, lista)
    except ValueError as ve:
        print("Eroare: ", ve)
        return lista


def ui_modifica_rezervare_2(ID, nume, clasa, pret, checkin_facut, lista):
    try:
        return modifica_rezervare(ID, nume, clasa, pret, checkin_facut, lista)
    except ValueError as ve:
        print("Eroare: ", ve)
        return lista


def run_menu_2(lista):
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
                    pret = c.split(",")[4]
                    checkin_facut = c.split(",")[5]
                    lista = ui_adauga_rezervare_2(ID, nume, clasa, pret, checkin_facut, lista)
                elif c[0:4] == "show":
                    show_all_2(lista)
                elif c[0:6] == "delete":
                    ID = c.split(",")[1]
                    lista = ui_sterge_rezervare_2(ID, lista)
                elif c[0:6] == "modify":
                    ID = c.split(",")[1]
                    nume = c.split(",")[2]
                    clasa = c.split(",")[3]
                    pret = c.split(",")[4]
                    checkin_facut = c.split(",")[5]
                    lista = ui_modifica_rezervare_2(ID, nume, clasa, pret, checkin_facut, lista)
                else:
                    print("Cerinta inexistenta! Mai incercati")


