from Domain.rezervare import get_clasa
from Logic.CRUD import adauga_rezervare
from Logic.functionality import trece_clasa_superioara


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

