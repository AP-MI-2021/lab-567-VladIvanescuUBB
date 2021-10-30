from Domain.rezervare import get_clasa, get_pret
from Logic.CRUD import adauga_rezervare
from Logic.functionality import trece_clasa_superioara, ieftinire


def test_trece_clasa_superioara():
    lista = []
    lista = adauga_rezervare("1", "Vlad", "business", 100, "da", lista)
    lista = adauga_rezervare("2", "Mark", "economy", 80, "nu", lista)
    lista = adauga_rezervare("3", "Mark", "economy plus", 110, "nu", lista)
    trece_clasa_superioara(lista, "Vlad")
    trece_clasa_superioara(lista, "Mark")

    assert get_clasa(lista[0]) == "business"
    assert get_clasa(lista[1]) == "economy plus"
    assert get_clasa(lista[2]) == "business"


def test_ieftinire():
    lista = []
    lista = adauga_rezervare("1", "Vlad", "business", 100, "da", lista)
    lista = adauga_rezervare("2", "Emma", "economy plus", 80, "da", lista)
    lista = adauga_rezervare("3", "Mark", "economy", 80, "nu", lista)
    ieftinire(lista, 25)

    assert get_pret(lista[0]) == 75
    assert get_pret(lista[1]) == 60
    assert get_pret(lista[2]) == 80

