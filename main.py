from Tests.test_all import run_all_tests
from UserInterface.console import run_menu
from UserInterface.console_2 import run_menu_2


def main():
    run_all_tests()
    optiune = input("Old menu or New menu? (old/new): ")
    while optiune != "old" and optiune != "new":
        print("Optiune invalida! Reincercati cu old/new.")
        optiune = input("Old menu or New menu? (old/new): ")
    if optiune == "old":
        run_menu([])
    else:
        run_menu_2([])


main()
