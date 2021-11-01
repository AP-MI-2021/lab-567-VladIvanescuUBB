from Domain.rezervare import get_clasa, get_pret, get_ID
from Logic.CRUD import adauga_rezervare
from Logic.functionality import trece_clasa_superioara, ieftinire, pret_max_clasa, ordonare_descrescator_pret


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


def test_pret_max_clasa():
    lista = []
    lista = adauga_rezervare("1", "Vlad", "economy", 100, "da", lista)
    lista = adauga_rezervare("2", "Emma", "economy plus", 80, "da", lista)
    lista = adauga_rezervare("3", "Mark", "economy", 80, "nu", lista)
    lista = adauga_rezervare("4", "Eric", "economy plus", 85, "da", lista)
    lista = adauga_rezervare("5", "Darius", "business", 200, "da", lista)

    assert pret_max_clasa(lista, "economy") == 100
    assert pret_max_clasa(lista, "economy plus") == 85
    assert pret_max_clasa(lista, "business") == 200


def test_ordonare_descrescator_pret():
    lista = []
    lista = adauga_rezervare("1", "Vlad", "economy", 100, "da", lista)
    lista = adauga_rezervare("2", "Emma", "economy plus", 150, "da", lista)
    lista = adauga_rezervare("3", "Darius", "business", 200, "da", lista)
    lista = ordonare_descrescator_pret(lista)

    assert get_ID(lista[0]) == "3"
    assert get_ID(lista[1]) == "2"
    assert get_ID(lista[2]) == "1"

    assert get_pret(lista[0]) == 200
    assert get_pret(lista[1]) == 150
    assert get_pret(lista[2]) == 100

