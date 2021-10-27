def creeaza_rezervare(ID, nume, clasa, pret, checkin_facut):
    """
    functia creeaza un dictionar care reprezinta o rezervare
    :param ID: string
    :param nume: string
    :param clasa: string (economy, economy plus, business)
    :param pret: float
    :param checkin_facut: string (da / nu)
    :return: un dictionar care contine o rezervare
    """
    return {
        "ID": ID,
        "nume": nume,
        "clasa": clasa,
        "pret": pret,
        "checkin_facut": checkin_facut
    }


# dict["ID"] -> ID


def get_ID(rezervare):
    """
    functia da ID-ul unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: ID-ul rezervarii
    """
    return rezervare["ID"]


def get_nume(rezervare):
    """
    functia da numele unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: numele rezervarii
    """
    return rezervare["nume"]


def get_clasa(rezervare):
    """
    functia da clasa unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: clasa rezervarii
    """
    return rezervare["clasa"]


def get_pret(rezervare):
    """
    functia da prteul unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: pretul rezervarii
    """
    return rezervare["pret"]


def get_checkin_facut(rezervare):
    """
    functia da checkin_facut-ul unei rezervari
    :param rezervare: dictionar ce contine o rezervare
    :return: checkin_facut-ul rezervarii
    """
    return rezervare["checkin_facut"]


def to_string(rezervare):
    return "ID: {}, nume: {}, clasa: {}, pret: {}, checkin_facut: {}".format(
        get_ID(rezervare),
        get_nume(rezervare),
        get_clasa(rezervare),
        get_pret(rezervare),
        get_checkin_facut(rezervare)
    )
