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

# otworzenie pliku ze statystyką i zapisanie kolejnego użycia pliku
with open('statystyka.txt', 'a+') as file:
    file.seek(0)  # ustawienie na pierwszym znaku
    linia = file.readline()
    linia = linia[30:]  # zaczytanie fragmentu tekstu od znaku 27 do końca
    linia_int = int(linia)+1  # zamiana fragmentu tesktu na liczbę
    file.truncate(30)  # usunięcie tekstu od 27 znaku do końca
    file.write(f'{linia_int}')
    print(f'Ilość uruchomień: {linia_int}')

# otworzenie i przeczytanie pliku tekstowego
with open('tekst.txt', 'r+', encoding='utf-8') as tekst:
    tekst_reader = tekst.read()

    # podział tekstu na wyrazy
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

    # ilość zdań
    znak = 0
    zdania = 0
    import string
    duze_litery = string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    cyfry = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for litera in list(tekst_reader):
        # ostatnia kropka, po której nie ma już dalszych znaków, dlatego dodaję +1
        if ile_znakow - znak < 2 and tekst_reader[znak] in ('.', '!', '?'):
            zdania += 1
        # zdanie kończące się kropką, a następne rozpoczynające się od nowej linii
        elif tekst_reader[znak] in ('.', '!', '?') and tekst_reader[(znak+1)] == '\n':
            zdania += 1
        # zdanie kończące się kropką, a następne rozpoczynające się od dużej litery bądź cudzysłowia
        elif tekst_reader[znak] in ('.', '!', '?') and tekst_reader[(znak+1)] == ' ' \
                and (tekst_reader[(znak+2)] in duze_litery or tekst_reader[(znak+2)] == '"'
                     or tekst_reader[(znak+2)] in cyfry):
            zdania += 1
        # wyjątek to zdanie ropoczynające sie od liczby
        znak += 1

    # pokaż statytykę przed zapisem do pliku
    wynik = (f"\nLiczb jest: {ile_liczb}, cyfr jest {ile_cyfr}.\n"
             f"Zdań jest: {zdania}, wyrazów jest: {ile_wyrazow}, liter jest {litera_alf}.\n"
             f"Znaków interpunkcyjnych jest: {ile_znakow-cyfra-litera_alf}.\n"
             f"łącznie wszystkich znaków jest: {ile_znakow}.\n")
    print(wynik)

    # zpis statystyk do pliku ze statystykami
    with open('statystyka.txt', 'a+', encoding='utf-8') as file:
        file.write(wynik)

    # ilość użyć poszczególnych cyfr
    zobacz = input("\nCzy chcesz zobaczyć statystykę cyfr? T/N")
    if zobacz.upper() == "T":
        with open('statystyka.txt', 'a+') as file:
            file.write(f"\nStatystyka cyfr w pliku:\n")
        # cyfry = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] - cyfry są podane wyżej
        for cyfra in cyfry:
            ile_razy = 0
            for litera in tekst_reader:
                if litera == str(cyfra):
                    ile_razy += 1
            wynik = f"Cyfra {cyfra} występuje {ile_razy} razy, procentowy udział cyfry w tekście" \
                    f" {int(ile_razy/ile_znakow*100)} %, w liczbach {int(ile_razy/ile_cyfr*100)} %"
            print(wynik)
            # zpis statystyki cyfr do osobnego pliku
            with open('statystyka.txt', 'a+', encoding='utf-8') as file:
                file.write(f"{wynik}\n")
    else:
        pass

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
        wynik = f"Dużych liter jest: {ile_duzych}, małych liter jest: {ile_malych}."
        print(wynik)
        with open('statystyka.txt', 'a+', encoding='utf-8') as file:
            file.write(f"\nStatystyka liter w pliku:\n{wynik}")

        # możliwość wyboru trybu case sensitivity
        import string
        sensitive = input("Czy uwzględniać małe i duże litery? T/N")
        if sensitive.upper() == "T":
            litery = string.ascii_letters  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
            tryb = "Wybrałeś rozróżnienie pomiędzy małymi i dużymi literami"
        elif sensitive.upper() == "N":
            litery = string.ascii_lowercase
            # lowercase: abcdefghijklmnopqrstuvwxyz,
            # uppercase: ABCDEFGHIJKLMNOPQRSTUVWXYZ
            tekst_reader = tekst_reader.lower()
            tryb = "Wybrałeś brak rozróżnienie pomiędzy małymi i dużymi literami"
        else:
            litery = string.ascii_lowercase
            tekst_reader = tekst_reader.lower()
            tryb = "Wpisałeś niepoprawną litere, więc wybieram za Ciebie " \
                   "brak rozróżnienia pomiędzy małymi i dużymi literami"

        with open('statystyka.txt', 'a+', encoding='utf-8') as file:
            file.write(f"\n{tryb}.")

        # policzenie ilosci uzyc poszczegolnych literek w tekscie
        for litera in litery:
            ile_razy = 0
            for litera_ciagu in tekst_reader:
                if litera_ciagu == str(litera):
                    ile_razy += 1
            wynik = f"Litera {litera} występuje {ile_razy} razy, procentowy udział cyfry w tekście" \
                    f" {int(ile_razy/ile_znakow*100)} %, w lietrach {int(ile_razy/litera_alf*100)} %"
            print(wynik)
            with open('statystyka.txt', 'a+', encoding='utf-8') as file:
                file.write(f"\n{wynik}")

        # znjadywanie tekstu podanego przez użytkoniwka
        zobacz = input("\nCzy chcesz znaleźć jakiś konkretny tekst? T/N")
        if zobacz.upper() == "T":
            with open('statystyka.txt', 'a+', encoding='utf-8') as file:
                file.write(f"\n\nZnajdywanie wyrazów podanych przez użytkownika\n")
            jeszcze_raz = "T"
            while jeszcze_raz == "T":
                znajdz = input("Podaj literkę, cyfrę albo słowo, które mam znaleźć: ")
                if sensitive.upper() == "T":
                    znajdywanie = tekst_reader.count(znajdz)
                    wynik = f"Wyraz:'{znajdz}' występuje w tekście {znajdywanie} razy."
                    print(wynik)
                else:
                    znajdz = znajdz.lower()
                    znajdywanie = tekst_reader.count(znajdz)
                    wynik = f"Wyraz:'{znajdz}' występuje w tekście {znajdywanie} razy."
                    print(wynik)
                # zpis statystyk do osobnego pliku
                with open('statystyka.txt', 'a+', encoding='utf-8') as file:
                    file.write(f"{wynik}\n")
                jeszcze_raz = input("\nCzy chcesz znaleźć kolejny wyraz? [T/N]").upper()
            else:
                pass
    else:
        pass
