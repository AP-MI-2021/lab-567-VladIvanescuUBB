from Domain.rezervare import get_ID, get_nume, get_clasa, get_pret, get_checkin_facut
from Logic.CRUD import adauga_rezervare, get_by_ID, sterge_rezervare, modifica_rezervare


def test_adauga_rezervare():
    lista = []
    lista = adauga_rezervare("1", "Vlad", "business", 100, "da", lista)
    lista = adauga_rezervare("2", "Mark", "business", 110, "nu", lista)

    assert len(lista) == 2
    assert get_ID(lista[0]) == "1"
    assert get_nume(lista[0]) == "Vlad"
    assert get_clasa(lista[1]) == "business"
    assert get_pret(get_by_ID("1", lista)) == 100
    assert get_checkin_facut(get_by_ID("2", lista)) == "nu"


def test_sterge_rezervare():
    lista = []
    lista = adauga_rezervare("1", "Vlad", "business", 100, "da", lista)
    lista = adauga_rezervare("2", "Mark", "business", 110, "nu", lista)

    lista = sterge_rezervare("1", lista)

    assert len(lista) == 1
    assert get_by_ID("1", lista) is None
    assert get_by_ID("2", lista) is not None


def test_modifica_rezervare():
    lista = []
    lista = adauga_rezervare("1", "Vlad", "business", 100, "da", lista)
    lista = adauga_rezervare("2", "Mark", "business", 110, "nu", lista)

    lista = modifica_rezervare("1", "Vlad", "economy", 35, "da", lista)

    assert get_clasa(lista[0]) == "economy"
    assert get_pret(lista[0]) == 35
    assert get_checkin_facut(lista[0]) == "da"
