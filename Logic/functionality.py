from Domain.rezervare import get_nume, get_clasa, get_checkin_facut, get_pret


def trece_clasa_superioara(lista, nume):
    """
    functia are ca efect trecerea tuturor rezervărilor făcute pe un nume dat la o clasă superioară
    :param lista: lista de rezervari
    :param nume: numele pe care sunt facute rezervarile
    :return: lista de rezervari modificata corespunzator
    """
    for rezervare in lista:
        if get_nume(rezervare) == nume:
            if get_clasa(rezervare) == "economy":
                rezervare[2] = "economy plus"
            elif rezervare[2] == "economy plus":
                rezervare[2] = "business"
    return lista


def ieftinire(lista, procentaj):
    """
    functia are ca efect ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj.
    :param lista: lista de rezervari
    :param procentaj: procentajul cu care se vor ieftini rezervarile (float)
    :return: lista de rezervari modificata corespunzator
    """
    if procentaj < 0 or procentaj > 100:
        raise ValueError("Procentajul trebuie sa fie intre 0 si 100!")
    for rezervare in lista:
        if get_checkin_facut(rezervare) == "da":
            rezervare[3] = rezervare[3] - ((rezervare[3] * procentaj) / 100)
    return lista


def pret_max_clasa(lista, clasa):
    """
    functia determina prețul maxim pentru o clasă.
    :param lista: lista de rezervari
    :param clasa: string
    :return: prețul maxim pentru clasa data.
    """
    for rezervare in sorted(lista, key=lambda rez: get_pret(rez), reverse=True):
        if get_clasa(rezervare) == clasa:
            return get_pret(rezervare)
    return None


def ordonare_descrescator_pret(lista):
    """
    functia ordoneaza rezervarile din lista descrescator dupa pret
    :param lista: lista de rezervari
    :return: lista ordonata descrescator dupa pretul rezervarilor
    """
    return sorted(lista, key=lambda rez: get_pret(rez), reverse=True)
