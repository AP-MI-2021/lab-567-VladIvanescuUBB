def trece_clasa_superioara(lista, nume):
    """
    functia are ca efect trecerea tuturor rezervărilor făcute pe un nume dat la o clasă superioară
    :param lista: lista de rezervari
    :param nume: numele pe care sunt facute rezervarile
    :return: lista de rezervari modificata corespunzator
    """
    for rezervare in lista:
        if rezervare["nume"] == nume:
            if rezervare["clasa"] == "economy":
                rezervare["clasa"] = "economy plus"
            elif rezervare["clasa"] == "economy plus":
                rezervare["clasa"] = "business"
    return lista
