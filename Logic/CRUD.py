from Domain.rezervare import creeaza_rezervare, get_ID


def adauga_rezervare(ID, nume, clasa, pret, checkin_facut, lista):
    """
    functia adauga o prajitura intr-o lista
    :param ID: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin_facut: string
    :param lista: lista de rezervari
    :return: o lista continand atat elementele vechi cat si noua rezervare
    """
    rezervare = creeaza_rezervare(ID, nume, clasa, pret, checkin_facut)
    return lista + [rezervare]


def get_by_ID(ID, lista):
    """
    functia da rezervarea cu ID-ul dat dintr-o lista
    :param ID: string
    :param lista: o lista de rezervari
    :return: rezervarea cu ID-ul dat din lista sau None, daca aceasta nu exista
    """
    for rezervare in lista:
        if get_ID(rezervare) == ID:
            return rezervare
    return None


def sterge_rezervare(ID, lista):
    """
    functia sterge o rezervare cu un ID dat din lista
    :param ID: string
    :param lista: o lista de rezervari
    :return: lista de rezervari fara rezervarea cu ID-ul dat
    """
    return [rezervare for rezervare in lista if get_ID(rezervare) != ID]


def modifica_rezervare(ID, nume, clasa, pret, checkin_facut, lista):
    """
    functia modifica o prajitura dupa ID
    :param ID: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin_facut: string
    :param lista: o lista de rezervari
    :return: lista de rezervari in care s-a modificat rezervarea cu ID-ul dorit
    """
    lista_noua = []
    for rezervare in lista:
        if get_ID(rezervare) == ID:
            rezervare_noua = creeaza_rezervare(ID, nume, clasa, pret, checkin_facut)
            lista_noua.append(rezervare_noua)
        else:
            lista_noua.append(rezervare)
    return lista_noua

