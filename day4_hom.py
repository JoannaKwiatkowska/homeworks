# rozwiązania zadań po spotkaniu 4


def rysowanie_prostokata():
    """Funkcja rysująca prostokąt o zadanych rozmiarach (wysokość i szerokość)
     za pomocą znaków | (bok) - (góra/dół) + (wierzchołek)"""
    print("Rysowanie prostokątu o zadanych parametrach")
    powtorz = "T"
    while powtorz == "T":
        bok_a = input("Podaj wymiar pierwszego boku: ")
        bok_b = input("Podaj wymiar drugiego boku: ")
        gora = "+" + int(bok_a) * "-" + "+"
        srodek = ""
        dol = "+" + int(bok_a) * "-" + "+"
        if bok_a.isdigit() is True and bok_b.isdigit() is True:  # sprawdzenie czy obie wartości to liczby całkowite
            for i in range(0, int(bok_b)):
                srodek = "|" + int(bok_a) * " " + "|"
            print(gora)
            print(srodek)
            print(dol)
        else:
            blad = "Wpisałeś nieporpawne wartości. Użyj tylko liczb całkowitych"
            print(blad)
        powtorz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
# ======================================================================================================================


def rysowanie_piramidy():
    """Program rysujący piramidę o określonej wysokości, np. dla 3
        #
       ###
      #####
    """
    print("\nRysowanie piramidy o określonej wysokości")
    jeszcze_raz = "T"
    while jeszcze_raz == "T":
        wysokosc = input("Ile pięter ma mieć piramida? ")
        if wysokosc.isdigit() is True:
            wysokosc = int(wysokosc)
            for i in range(0, wysokosc):
                piramida = " "*(wysokosc-i-1)+"#"+"#"*i*2
                print(piramida)
        else:
            blad = f"{wysokosc} to nie jest liczba całkowita. Jakby miałabym narysować półpiętra? :)"
            print(blad)
        jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
# ======================================================================================================================


def kalkulator_celsjusz_fahenheit():
    """Kalkulator do przeliczania stopni Celsjusza na Fahrenheita"""
    print("\nPrzeliczanie stopni Celsjusza na Fahrenheita")
    jeszcze_raz = "T"
    while jeszcze_raz == "T":
        celsjusz_str = input("Podaj temperaturę w stopniach Celsjusza: ")
        celsjusz = ""
        if celsjusz_str.isdigit() is True:  # tutaj powinno być sprawdzenie czy liczba jest float a nie integer
            celsjusz = float(celsjusz_str)
            wzor = 32 + 1.8 * celsjusz  # jak podać wzór jako zawartość, a nie jako wynik do zmiennej wynik?
            fahrenheit_temp = round(wzor, 1)
            wynik = f"{celsjusz} stopni Celsjusza to {fahrenheit_temp} w stopaniach Fahrenheita." \
                    f"Wzór to: 32 + 1.8 * celsjusz "
        else:
            wynik = f"{celsjusz} to nie jest poprwana temperatura"
        print(wynik)
        jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
# =======================================================================================================================


def kalkulator_fahenheit_celsjusz():
    """Kalkulator do przeliczania stopni Fahrenheita na Celsjusza"""
    print("\nPrzeliczanie stopni Fahrenheita na Celsjusza")
    jeszcze_raz = "T"
    while jeszcze_raz == "T":
        fahrenheit = input("Podaj temperaturę w stopniach Fahrenheita: ")
        if fahrenheit.isdigit() is True:  # tutaj powinno być sprawdzenie czy liczba jest float a nie integer
            celsjusz_temp = round(((float(fahrenheit) - 32) / 1.8), 1)
            wynik = f"{fahrenheit} stopni Fahrenheit to {celsjusz_temp} w stopaniach Celsjusza." \
                    f" Wzór to: (Fahrenheit-32)/1.8"  # jak podać wzór z zmiennej Celsjusz_temp?
        else:
            wynik = f"{fahrenheit} to nie jest poprwana temperatura"
        print(wynik)
        jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
# ======================================================================================================================


def cyfra_pierwsza_ostatnia():
    """Program, który podaje pierwszą i ostatnią cyfrę podanej liczby"""
    print("\nPierwsza i ostatnia cyfra podanej liczby")
    jeszcze_raz = "T"
    while jeszcze_raz == "T":
        liczba = input("Podaj dwolną liczbę całkowitą: ")
        if liczba.isdigit() is False:
            wynik = f"{liczba} to nie jest liczba całkowita"
        else:
            wynik = f"Wpisano liczbę {liczba}. Cyfra pierwsza to {liczba[0]}, a cyfra ostatnia to {liczba[-1]}."
        print(wynik)
        jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
# ======================================================================================================================


def binara_na_dziesietna():  # to jest do dopracowania
    """Przeliczanie liczy binarnej na dziesiętną"""
    jeszcze_raz = "T"
    while jeszcze_raz == "T":
        binarna = input("Podaj liczbę binarną do przeliczenia na dziesiętną: ")
        wynik = int(binarna[-1]) ** 0  # ostatnia liczba do potęgi zerowej 0**=0, dowolna inna liczba**0=1
        ilosc_0 = binarna.count("0")
        ilosc_1 = binarna.count("1")
        dlugosc_liczby = len(binarna)
        licznik = 1
        if ilosc_0 == dlugosc_liczby or ilosc_1 == dlugosc_liczby or ilosc_0+ilosc_1 == dlugosc_liczby:
            # sprawdzam czy liczba składa się z samych znaków 0 i 1
            while licznik in range(1, len(binarna)):
                dziesietna = int(binarna[-(licznik + 1)]) * 2 ** licznik
                wynik = wynik + dziesietna
                licznik += 1
            wynik_obliczen = f"Liczba binarna {binarna} to liczba dziesiętna {wynik}"
        else:
            wynik_obliczen = f"Liczba {binarna} nie jest liczbą binarną"
        print(wynik_obliczen)
        jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
# ======================================================================================================================


def rok_przestepny():
    """Program do sprawdzania czy podany rok jest rokiem przestępnym.
    Rok przestęny jest podzielny przez 4 i nie jest podzielny przez 100
    lub jest przestępny jeżeli rok jest podzielny przez 400."""
    jeszcze_raz = "T"
    while jeszcze_raz == "T":
        rok = input("Podaj rok do sprawdzenia: ")
        if len(rok) != 4 or rok.isdigit() is False:  # sprawdza czy są 4 znaki oraz czy znaki są liczbami
            wynik = f"{rok} to nie jest poprawny rok"
        elif (int(rok) % 4 == 0 and int(rok) % 100 != 0) or int(rok) % 400 == 0:
            wynik = f"Rok {rok} jest przestępny"
        else:
            wynik = f"Rok {rok} nie jest przestępny"
        print(wynik)
        jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
# ======================================================================================================================


def kalkulator_pieskie_lata():
    """Kalkulator do wyliczania wieku psa."""
    jeszcze_raz = "T"
    while jeszcze_raz == "T":
        wiek_psa_str = input("Podaj wiek psa, a ja ci przeliczę na ludzkie lata. Podaj liczbę całkowitą ")
        if wiek_psa_str.isdigit() is False:
            wynik = f"{wiek_psa_str} to nie jest liczba całkowita"
        else:
            # obliczanie wieku psa
            wiek_psa_int = int(wiek_psa_str)
            if wiek_psa_int <= 2:  # przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku
                ludzkie_lata = wiek_psa_int * 10.5
            else:  # po drugim roku psi rok to 4 ludzkie lata
                ludzkie_lata = int(2 * 10.5) + (wiek_psa_int - 2) * 4
            # sprawdzanie poprawnej odmiany lat dla lat psich
            odmiana_liczby_pies = "lat"  # w liczbach po cyfrach 0, 1 i od 5 do 9 występuje dopełniacz liczby mnogiej
            if wiek_psa_int == 1:
                odmiana_liczby_pies = "rok"
            elif wiek_psa_str[-1] in ("2", "3", "4"):  # w liczbach po cyfrach 2,3 i 4 występuje rzeczownik w mianowniku
                odmiana_liczby_pies = "lata"
            # sprawdzanie poprawnej odmiany lat dla lat ludzkich
            odmiana_liczby_czlowiek = "lat"
            if str(ludzkie_lata)[-1] in ("2", "3", "4"):
                odmiana_liczby_czlowiek = "lata"
            wynik = f"{wiek_psa_int} {odmiana_liczby_pies} dla psa to ludzkie {ludzkie_lata} {odmiana_liczby_czlowiek}"
        print(wynik)
        jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
# ======================================================================================================================


def odczyty_temperatury():
    """Zmienna dane zawiera 24 odczyty temperatury z 24 godzin.
    Każde 4 znaki to jeden odczyt w setnych stopni Celsjusza, tzn "2150" to 21.50°C
    Pomiary są dokonane o pełnych godzinach od 00:00 do 23:00.
    Dla odczytów niższych niż lub równych 20°C dodawany jest "<tabulator>!"
    Dla odczytów niższych niż lub równych 18,5°C dodany jeest dodatkowy wykrzyknik"""
    jeszcze_raz = "T"
    while jeszcze_raz == "T":
        dane = "215021482120211921002076207620502065202020152010200520002001199319901950183417501744186019462010"
        print("(...)")
        for odczyt in range(0, 24):  # gdyby string nie był znanej długości wtedy range(0, len(dane), 4)
            poczatek_zakresu = odczyt * 4  # co 4 cyfry ropzoczyna się nowy odczyt
            srodek_zakresu = poczatek_zakresu + 2
            koniec_zakresu = poczatek_zakresu + 4
            temperatura = float(f"{dane[poczatek_zakresu:srodek_zakresu]}.{dane[srodek_zakresu:koniec_zakresu]}")
            temp_float = "%0.2f" % temperatura  # wyświetlenie liczby do 2 miejsc po przecinku
            tab = ""
            odczyt_format = odczyt
            if temperatura <= 18.5:
                tab = "\t!!"
            elif temperatura <= 20:
                tab = "\t!"
            if odczyt <= 9:
                odczyt_format = f"0{odczyt}"  # wyświetlenie dodatkowego 0 z przodu dla cyfr do 10
            wiersz_string = f"{odczyt_format}:00\t{temp_float}\u00b0C{tab}"  # \u00b0 to znak unicode stopni Celsjusza
            print(wiersz_string)
        print("(...)")
        jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
# ======================================================================================================================


def rozmieniarka_pieniedzy():
    """Program przyjmuje kwotę w parametrze i wylicza jak rozmienić to na monety: 5, 2, 1, 0.5, 0.2, 0.1
    wydając ich jak najmniej."""
    jeszcze_raz = "T"
    while jeszcze_raz == "T":
        monety = [5, 2, 1, 0.5, 0.2, 0.1]
        kwota = float(input("Ile chcesz rozmienić? Możesz podać kwotę w zaokrągleniu do 10 groszy "))
        for moneta in monety:
            rozmienione = kwota//moneta  # znak // dzieli obcniając resztę (nazwa: floor division lub integer division)
            kwota = kwota - rozmienione*moneta  # to jest reszta która została do rozmienienia
            do_wydania = f"Monet {moneta} zł: {rozmienione}"
            print(do_wydania)
        reszta = round(kwota, 2)
        if reszta != 0:
            reszta = f"Nie podałeś liczby zaokrąglonej do 10 gr, więc reszta {reszta} zł jest dla mnie"
            print(reszta)
        jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
# ======================================================================================================================


def rysowanie_listy():
    """Program który przyjmie w parametrze dowolną listę np ['col1', 'col2', 'col3'] i wyświetla:
    +------+------+------+
    | col1 | col2 | col3 |
    +------+------+------+
    Szerokość kolumn jest zawsze równa bez względów na zawartość, tekst wyrównany do lewej.
    Maksymalna szerokość kolumny to 30 znaków, dłuże teksty są przycinane i kończą sie trzema kropkami.
    Dla list zagnieżdżonych narysuje się tabela z odpowiednią ilością wierszy i kolumn"""
    jeszcze_raz = "T"
    while jeszcze_raz == "T":
        wersja = input("Którą wersję chcesz zobaczyć: jednowierszowa lista czy matryca? W/M").capitalize()
        ramka = "+" + 30 * "-"
        if wersja == "W":  # wersja z listą w jednym wierszu
            lista = ['tutaj jest komórka 1', 'tutaj jest komórka 2', 'tutaj jest komórka 3 - ostatnia na liście']
            dlugosc_listy = len(lista)
            srodek_lista = ""
            i = 0
            for opis in lista:
                if len(opis) > 30:
                    srodek = "|" + opis[:27] + "..."
                else:
                    srodek = "|" + opis + (30 - len(lista[i])) * " "
                srodek_lista = srodek_lista + srodek
                i += 1
            print(ramka * dlugosc_listy + "+")
            print(srodek_lista + "|")
            print(ramka * dlugosc_listy + "+")
        if wersja == "M":  # wersja z matrycą dla list zagnieżdżonych
            lista = [["opis komórki 00 bardzo długi opis", "opis komóki 01", "opis komórki 02"],
                     ["opis komórki 10", "opis komóki 11", "opis komórki 12"],
                     ["opis komórki 20", "opis komóki 21", "opis komórki 22"]]
            j = 0
            for element in lista:
                i = 0
                srodek_lista = ""
                for opis in element:
                    if len(opis) > 30:
                        srodek = "|" + opis[:27] + "..."
                    else:
                        srodek = "|" + opis + (30 - len(opis)) * " "
                    srodek_lista = srodek_lista + srodek
                    i += 1
                if j == 0:
                    print(ramka * i + "+")
                    print(srodek_lista + "|")
                    print(ramka * i + "+")
                elif j >= 1:
                    print(srodek_lista + "|")
                    print(ramka * i + "+")
                j += 1
        jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
# ======================================================================================================================


lista_programów = ["Witaj w Multitool. Wybierz program który cię interesuje: ",
                  "1) Rysowanie prostokątu o zadanych parametrach",
                  "2) Rysowanie piramidy o określonej wysokości",
                  "3) Przeliczanie C->F",
                  "4) Przeliczanie F->C",
                  "5) Pierwsza i ostatnia cyfra z liczby",
                  "6) Przeliczanie liczy binarnej na dziesiętną",
                  "7) Sprawdenie czy rok jest przestępny",
                  "8) Kalkulator do wyliczania wieku psa",
                  "9) Odczytywanie_temperatury",
                  "10) Rozmienianie pieniędzy",
                  "11) Rysowanie listy",
                  "R) Wybierz program losowo bo nie wiem czego szukam:)",
                  "X) Wyjście z programu"]
zapytaj_ponownie = "T"
while zapytaj_ponownie == "T":
    print(f"\n".join(i for i in lista_programów) + "\n")  # rozdzielam elementy listy nową linią i kończę pustą linią
    wybor = input("Twój wybór: ")
    if wybor.isalpha():
        wybor_litera = wybor.upper()
        if wybor_litera == "R":
            from random import randint
            los = randint(1, 11)  # losowy wybór programu
            wybor = str(los)  # zamiana na str, ponieważ funkcja isdigit() w kolejnym if działa tylko dla str
            info = f"Wybrałeś losowy wybór programu. Przejdziesz teraz do zadania {wybor}\t"
        elif wybor_litera == "X":
            info = "Koniec. Dzięki, że tu zajrzałeś 😉"
            print(info)
            break
        else:
            info = "Twój wybór jest niepoprawny"
        print(info)
    if wybor.isdigit():
        wybor_liczba = int(wybor)
        if wybor_liczba == 1:
            rysowanie_prostokata()
        elif wybor_liczba == 2:
            rysowanie_piramidy()
        elif wybor_liczba == 3:
            kalkulator_celsjusz_fahenheit()
        elif wybor_liczba == 4:
            kalkulator_fahenheit_celsjusz()
        elif wybor_liczba == 5:
            cyfra_pierwsza_ostatnia()
        elif wybor_liczba == 6:
            binara_na_dziesietna()
        elif wybor_liczba == 7:
            rok_przestepny()
        elif wybor_liczba == 8:
            kalkulator_pieskie_lata()
        elif wybor_liczba == 9:
            odczyty_temperatury()
        elif wybor_liczba == 10:
            rozmieniarka_pieniedzy()
        elif wybor_liczba == 11:
            rysowanie_listy()
        else:
            info = "Twój wybór jest niepoprawny"
            print(info)
    zapytaj_ponownie = input("\nCzy chcesz uruchomić inny program? [T/N]").upper()
    info = "Koniec. Dzięki, że tu zajrzałeś 😉"
    print(info)
