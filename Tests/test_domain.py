from Domain.rezervare import creeaza_rezervare, get_ID, get_nume, get_clasa, get_pret, get_checkin_facut


def test_rezervare():
    rezervare = creeaza_rezervare("1", "Vlad", "business", 100, "da")
    assert get_ID(rezervare) == "1"
    assert get_nume(rezervare) == "Vlad"
    assert get_clasa(rezervare) == "business"
    assert get_pret(rezervare) == 100
    assert get_checkin_facut(rezervare) == "da"
