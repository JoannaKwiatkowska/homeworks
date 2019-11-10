# 1) Napisz program, który poda statystki dowolnego tekstu pobranego z pliku,
#    wypisze takie dane jak: ilość użyć poszczególnych literek i cyfr, ilość wyrazów, zdań etc.
#    Nie będzie możliwość wyboru tryb case sensitivity.
#    Niech program tworzy też plik ze statystyką swojej pracy. Czyli np:
#    "
#    Ilość uruchomień programu:
#    10
#    Przeanalizowanych znaków:
#    1223435991
#    Znalezionych wyrazów:
#    2399
#    Znalezionych liczb:
#    122
#    Znalezionych małych liter:
#    68923455
#    etc
#    "
#
#    Przydatny generator tekstów: http://lipsum.pl/

with open('tekst.txt', 'r+', encoding='utf-8') as tekst:
    tekst_reader = tekst.read()

    # ilość użyć poszczególnych literek i cyfr, ilość wyrazów, zdań etc.
    # znajdz = input("Podaj literkę, cyfrę albo słowo, które mam znaleźć: ")
    # znajdywanie = tekst_rader.count(znajdz)
    # print(f"W tekście '{znajdz}' występuje {znajdywanie} razy")

    # ilość zdań - trzeba usnąć z tego dodać wszystkie skróty polskie koczące się kropką
    zdania = tekst_reader.count(".") + tekst_reader.count("!") + tekst_reader.count("?") + tekst_reader.count("...")
    print(f"Zdań jest maksymalnie: {zdania}")
    # uwzględnianie skrótów i skrótowców w jezyku polskim?
    # zdań będzie nie więcej niż jest dużych znaków, jeżeli zdania nie zaczynaja się od liczby

    # ilość wyrazów i liczb
    wyrazy = tekst_reader.split()  # podział teksu na wyrazy metodą split

    # liczby
    # trzeba pozbyć się znaków interpunkcyjnych z liczb, bo np. "123." to nie jest liczba
    cyfra = 0
    ile_liczb = 0
    for slowo in wyrazy:
        for litera in slowo:  # jeżeli jakakolwiek litera w wyrazie jest cyfrą to przyjmij, że to liczba
            cyfra = 0
            if litera.isdigit() is True:
                cyfra += 1
        if cyfra >= 1:
            ile_liczb += 1
    # cyfry
    ile_cyfr = 0
    for slowo in wyrazy:
        for litera in slowo:  # jeżeli jakakolwiek litera w wyrazie jest cyfrą to przyjmij, że to liczba
            if litera.isdigit() is True:
                ile_cyfr += 1
    # słowa - słowami nie są znaki iterpunkcyjne np. " - "
    litera_alf = 0
    ile_wyrazow = 0  # zadziała tak samo jak len(wyrazy)
    for slowo in wyrazy:
        for litera in slowo:  # jeżeli jakakolwiek litera w wyrazie jest litera to przyjmij, że to wyraz
            litera_alf = 0
            if litera.isalpha() is True:
                litera_alf += 1
        if litera_alf >= 1:
            ile_wyrazow += 1
    # litery
    litera_alf = 0
    for slowo in wyrazy:
        for litera in slowo:  # jeżeli jakakolwiek litera w wyrazie jest litera to przyjmij, że to wyraz
            if litera.isalpha() is True:
                litera_alf += 1
    # ilość znaków ogólnie
    znaki = list(tekst_reader)  # podział teksu na litery metodą list
    ile_znakow = len(znaki)
    print(f"Liczb jest: {ile_liczb}, cyfr jest {ile_cyfr}.\n"
          f"Wyrazów jest: {ile_wyrazow}, liter jest {litera_alf}.\n"
          f"Znaków interpunkcyjnych jest: {ile_znakow-cyfra-litera_alf}.\n"
          f"Lacznie wszystkich znakow jest: {ile_znakow}")

    # ilość użyć poszczególnych cyfr
    zobacz = input("\nCzy chcesz zobaczyć statystykę cyfr? T/N")
    if zobacz.upper() == "T":
        cyfry = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for cyfra in cyfry:
            ile_razy = 0
            for litera in tekst_reader:
                if litera == str(cyfra):
                    ile_razy += 1
            wynik = f"Cyfra {cyfra} występuje {ile_razy} razy, procentowy udział cyfry w tekście" \
                    f" {int(ile_razy/ile_znakow*100)} %, w liczbach {int(ile_razy/ile_cyfr*100)} %"
            print(wynik)
    elif zobacz.upper() == "N":
        pass
    else:
        print("Wpisałeś niepoprawną literę, więc ci ją pokażę")

    # ilość użyć poszczególnych literek
    zobacz = input("\nCzy chcesz zobaczyć statystykę liter? T/N")
    if zobacz.upper() == "T":

        # ilość małych i dużych liter oraz cyfr i znaków interpukcyjnych
        ile_malych = 0
        ile_duzych = 0
        for litera in znaki:
            if litera.islower() is True:
                ile_malych += 1
            if litera.isupper() is True:
                ile_duzych += 1
        print(f"Dużych liter jest {ile_duzych}, małych liter jest: {ile_malych}")

        # możliwość wyboru trybu case sensitivity
        import string
        sensitive = input("Czy uwzględniać małe i duże litery? T/N")
        if sensitive.upper() == "T":
            litery = string.ascii_letters  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
        elif sensitive.upper() == "N":
            litery = string.ascii_lowercase
            # lowercase: abcdefghijklmnopqrstuvwxyz,
            # uppercase: ABCDEFGHIJKLMNOPQRSTUVWXYZ
            tekst_reader = tekst_reader.lower()
        else:
            litery = string.ascii_lowercase
            tekst_reader = tekst_reader.lower()
            print("Wpisałeś niepoprawną literę, więc wybieram za Ciebie brak trybu case sensitivity")

        # policzenie ilosci uzyc poszczegolnych literek w tekscie
        for litera in litery:
            ile_razy = 0
            for litera_ciagu in tekst_reader:
                if litera_ciagu == str(litera):
                    ile_razy += 1
            wynik = f"Literaz {litera} występuje {ile_razy} razy, procentowy udział cyfry w tekście" \
                    f" {int(ile_razy/ile_znakow*100)} %"
            print(wynik)
    elif zobacz.upper() == "N":
        pass
    else:
        print("Wpisałeś niepoprawną literę, więc ci ją pokażę")
