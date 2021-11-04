from Tests.test_CRUD import test_adauga_rezervare, test_sterge_rezervare, test_modifica_rezervare
from Tests.test_domain import test_rezervare
from Tests.test_functionality import test_trece_clasa_superioara, test_ieftinire, test_pret_max_clasa, \
    test_ordonare_descrescator_pret, test_suma_pret


def run_all_tests():
    test_rezervare()
    test_adauga_rezervare()
    test_sterge_rezervare()
    test_modifica_rezervare()
    test_trece_clasa_superioara()
    test_ieftinire()
    test_pret_max_clasa()
    test_ordonare_descrescator_pret()
    test_suma_pret()
