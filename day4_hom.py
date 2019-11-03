# Od dziś też będę zwaracał uwagę na to czy nie tylko kod działa ale:
# a) czy składanie jest ładna i zgodna ze standardami
# b) czy kod jest zabezpieczony przed wprowadzaniem niepoprawnych danych
#    (np jeśli prosimy o liczbę a dostaniemy znaki poprośmy użytkownika o podanie danej jeszcze raz)
# c) czy metody są udokumentowane a co ciekawsze fragmentu kodu opatrzone komentarzem.
# d) parametryzacja, im większy wpływ na program i jakieś parametry tym fajniej :)
# e) wydzielanie uniwersalnych fragmentów kodów do osobnych funckji
#
# Zadania:
# 1) Prośba o przepisanie dotychczasowych proagramów z wykorzystaniem definiowania własnych funkcji i wytycznych powyżej
# 2) Stworzenie "programu nakładki" na dotychczasowe programiki.
#    Po wyborze danego programu z "menu" uruchomi się odpowiedni i po wykonaniu danej operacji zapyta czy wykonać inny program.
#    Sugeruje by każdy "podprogram był oddzielną funkcją".
#    Miejmy na uwadze to by w przyszłości ten program rozwijać podpinając kolejny "podprogram" - powinno to być najprostsze jak się da (np tylko zmiana menu i jakiegoś jednego ifa?:) )

#=======================================================================================================================
def rysowanie_prostokąta():
    """Funkcja rysująca prostokąt o zadanych rozmiarach (wysokość i szerokość)
     za pomocą znaków | (bok) - (góra/dół) + (wierzchołek)"""
    print("Rysowanie prostokątu o zadanych parametrach")
    powtórz_zadanie = "T"
    while powtórz_zadanie == "T":
        bok_a = input("Podaj wymiar pierwszego boku: ")
        bok_b = input("Podaj wymiar drugiego boku: ")
        if bok_a.isdigit() == True and bok_b.isdigit() == True:  # sprawdzenie czy obie wartości to liczby całkowite
            print("+" + int(bok_a) * "-" + "+")
            for i in range(0, int(bok_b)):
                print("|" + int(bok_a) * " " + "|")
            print("+" + int(bok_a) * "-" + "+")
        else:
            print("Wpisałeś nieporpawne wartości. Użyj tylko liczb całkowitych")
        powtórz_zadanie = input("\nCzy chcesz powtórzyć? [T/N]").upper()
#=======================================================================================================================
def rysowanie_piramidy():
    """Program rysujący piramidę o określonej wysokości, np. dla 3
        #
       ###
      #####
    """
    print("\nRysowanie piramidy o określonej wysokości")
    jeszcze_raz = "T"
    while jeszcze_raz == "T":
        wysokość = input("Ile pięter ma mieć piramida? ")
        if wysokość.isdigit() == True:
            wysokość = int(wysokość)
            for i in range(0, wysokość):
                print(" "*(wysokość-i-1)+"#"+"#"*i*2)
        else:
            print(f"{wysokość} to nie jest liczba całkowita. Jakby miałabym narysować półpiętra? :)")
        jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
#=======================================================================================================================
def kalkulator_Celsjusz_Fahenheit():
    """Kalkulator do przeliczania stopni Celsjusza na Fahrenheita"""
    print("\nPrzeliczanie stopni Celsjusza na Fahrenheita")
    jeszcze_raz = "T"
    while jeszcze_raz == "T":
        Celsjusz_str = input("Podaj temperaturę w stopniach Celsjusza: ")
        if Celsjusz_str.isdigit() == True:  # tutaj powinno być sprawdzenie czy liczba jest float a nie integer
            Celsjusz = float(Celsjusz_str)
            wzór = 32 + 1.8 * Celsjusz  # jak podać wzór jako zawartość, a nie jako wynik do zmiennej wynik?
            Fahrenheit_temp = round(wzór, 1)
            wynik = f"{Celsjusz} stopni Celsjusza to {Fahrenheit_temp} w stopaniach Fahrenheita. {wzór}"
        else:
            wynik = f"{Celsjusz} to nie jest poprwana temperatura"
        print(wynik)
        jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
#=======================================================================================================================
def kalkulator_Fahenheit_Celsjusz():
    """Kalkulator do przeliczania stopni Fahrenheita na Celsjusza"""
    print("\nPrzeliczanie stopni Fahrenheita na Celsjusza")
    jeszcze_raz = "T"
    while jeszcze_raz == "T":
        Fahrenheit = input("Podaj temperaturę w stopniach Fahrenheita: ")
        if Fahrenheit.isdigit() == True:  # tutaj powinno być sprawdzenie czy liczba jest float a nie integer
            Celsjusz_temp = round(((float(Fahrenheit) - 32) / 1.8), 1)
            wynik = f"{Fahrenheit} stopni Fahrenheit to {Celsjusz_temp} w stopaniach Celsjusza. Wzór to: (Fahrenheit-32)/1.8"
            # jak poadż wzór z zmiennej Celsjusz_temp?
        else:
            wynik = f"{Fahrenheit} to nie jest poprwana temperatura"
        print(wynik)
        jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
#=======================================================================================================================
def cyfra_pierwsza_ostatnia():
    """Program, który podaje pierwszą i ostatnią cyfrę podanej liczby"""
    print("\nPierwsza i ostatnia cyfra podanej liczby")
    jeszcze_raz = "T"
    while jeszcze_raz == "T":
        liczba = input("Podaj dwolną liczbę całkowitą: ")
        if liczba.isdigit() == False:
            wynik = f"{liczba} to nie jest liczba całkowita"
        else:
            print(f"Wpisano liczbę {liczba}")
            cyfra_pierwsza = liczba[0]
            cyfra_ostatania = liczba[-1]
            wynik = f"Pierwsza cyfra to {cyfra_pierwsza}, ostatnia cyfra to {cyfra_ostatania}"
        print(wynik)
        jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
#=======================================================================================================================
def binara_na_dziesiętną(): #to jest do dopracowania
    """Przeliczanie liczy binarnej na dziesiętną"""
    jeszcze_raz = "T"
    while jeszcze_raz == "T":
        binarna = input("Podaj liczbę binarną do przeliczenia na dziesiętną: ")
        licznik = int(1)
        wynik = int(binarna[-1]) ** 0  # ostatnia liczba do potęgi zerowej 0**=0, dowolna inna liczba**0=1
        # niebinarne = ["2","3","4","5","6","7","8","9"]
        if "2" not in list(binarna) and "3" not in list(binarna) and "4" not in list(binarna) and "5" not in list(
                binarna) \
                and "6" not in list(binarna) and "7" not in list(binarna) and "8" not in list(
            binarna) and "9" not in list(binarna):
            # binarna.find("1") != 0 or binarna.find("0") != 0:
            while licznik in range(1, len(binarna)):
                dziesiętna = int(binarna[-(licznik + 1)]) * 2 ** (licznik)  # dlaczego 1 do potęgi 0 daje zero?
                wynik = wynik + dziesiętna
                licznik = licznik + 1
            print(f"Liczba binarna {binarna} to liczba dziesiętna {wynik}")
        else:
            print(f"Liczba {binarna} nie jest liczbą binarną")
        # print(f"Liczba binarna {binarna} to liczba dziesiętna {wynik}")

        jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
#=======================================================================================================================
def rok_przestępny():
    """Program do sprawdzania czy podany rok jest rokiem przestępnym.
    Rok przestęny jest podzielny przez 4 i nie jest podzielny przez 100
    lub jest przestępny jeżeli rok jest podzielny przez 400."""
    jeszcze_raz = "T"
    while jeszcze_raz == "T":
        rok = input("Podaj rok do sprawdzenia: ")
        if len(rok) != 4 or rok.isdigit() == False:  # sprawdza czy są 4 znaki oraz czy znaki są liczbami
            wynik = f"{rok} to nie jest poprawny rok"
        elif (int(rok) % 4 == 0 and int(rok) % 100 != 0) or int(rok) % 400 == 0:
            wynik = f"Rok {rok} jest przestępny"
        else:
            wynik = f"Rok {rok} nie jest przestępny"
        print(wynik)
        jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
#=======================================================================================================================
def kalkulator_piskie_lata():
    """Kalkulator do wyliczania wieku psa."""
    jeszcze_raz = "T"
    while jeszcze_raz == "T":
        wiek_psa_str = input("Podaj wiek psa, a ja ci przeliczę na ludzkie lata. Podaj liczbę całkowitą ")
        if wiek_psa_str.isdigit() == False:
            wynik=f"{wiek_psa_str} to nie jest liczba całkowita"
        else:
            # obliczanie wieku psa
            wiek_psa_int = int(wiek_psa_str)
            if wiek_psa_int <= 2: # przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku
                ludzkie_lata = wiek_psa_int * 10.5
            else:  # po drugim roku psi rok to 4 ludzkie lata
                ludzkie_lata = int(2 * 10.5) + (wiek_psa_int - 2) * 4
            # sprawdzanie poprawnej odmiany liczb dla lat psich
            odmiana_liczby_pies = "lat" # w liczbach po cyfrach 0, 1 i od 5 do 9 występuje dopełniacz liczby mnogiej
            if wiek_psa_int == 1:
                odmiana_liczby_pies = "rok"
            elif wiek_psa_str[-1] in ("2","3","4"): # w liczbach po cyfrach 2,3 i 4 występuje rzeczownik w mianowniku
                odmiana_liczby_pies = "lata"
            # sprawdzanie poprawnej odmiany liczb dla lat ludzkich
            odmiana_liczby_człowiek = "lat"
            if str(ludzkie_lata)[-1] in ("2","3","4"):
                odmiana_liczby_człowiek = "lata"
            wynik = f"{wiek_psa_int} {odmiana_liczby_pies} dla psa to ludzkie {ludzkie_lata} {odmiana_liczby_człowiek}"
        print(wynik)
        jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
#=======================================================================================================================
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
        for odczyt in range(0, 24): #gdyby string nie był znanej długości wtedy range(0, len(dane), 4)
            początek_zakresu = odczyt*4 #co 4 cyfry ropzoczyna się nowy odczyt
            środek_zakresu = początek_zakresu+2
            koniec_zakresu = początek_zakresu+4
            temperatura = float(f"{dane[początek_zakresu:środek_zakresu]}.{dane[środek_zakresu:koniec_zakresu]}")
            temp_float = "%0.2f" %temperatura #wyświetlenie liczby do 2 miejsc po przecinku
            tab = ""
            odczyt_format = odczyt
            if temperatura <= 18.5:
                tab = "\t!!"
            elif temperatura <= 20:
                tab = "\t!"
            else:
                tab
            if odczyt <= 9:
                odczyt_format = f"0{odczyt}" #wyświetlenie dodatkowego 0 z przodu dla cyfr do 10
            else:
                odczyt_format
            wiersz_string = f"{odczyt_format}:00\t{temp_float}\u00b0C{tab}"  # \u00b0 to znak unicode stopni Celsjusza
            print(wiersz_string)
        print("(...)")
        jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
#=======================================================================================================================
def rozmieniarka_pieniędzy():
    """Program przyjmuje kwotę w parametrze i wylicza jak rozmienić to na monety: 5, 2, 1, 0.5, 0.2, 0.1
    wydając ich jak najmniej."""
    jeszcze_raz = "T"
    while jeszcze_raz == "T":
        monety = [5,2,1,0.5,0.2,0.1]
        kwota = float(input("Ile chcesz rozmienić? Możesz podać kwotę w zaokrągleniu do 10 groszy "))
        for moneta in monety:
            rozmienione = kwota//moneta # znak // dzieli obcniając resztę (nazwa to floor division lub integer division)
            kwota = kwota - rozmienione*moneta # to jest reszta która została do rozmienienia
            do_wydania = f"Monet {moneta} zł: {rozmienione}"
            print(do_wydania)
        reszta = round(kwota,2)
        if reszta != 0:
            reszta = f"Nie podałeś liczby zaokrąglonej do 10 gr, więc reszta {reszta} zł jest dla mnie"
            print(reszta)
        jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
#=======================================================================================================================
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

        wersja = input("Zrobiłam dwie wersja - na listę w jednym wierszu i matrycę dla list zagnieżdżonych. W/M").capitalize()
        if wersja == "W":  # wersja z listą w jednym wierszu
            lista = ['tutaj jest komórka 1', 'tutaj jest komórka 2', 'tutaj jest komórka 3 - ostatnia na liście']
            długość_listy = len(lista)
            góra = "+" + 30 * "-"
            środek_lista = ""
            dół = "+" + 30 * "-"
            i = 0
            for opis in lista:
                if len(lista[i]) > 30:
                    środek = "|" + lista[i][:27] + "..."
                else:
                    środek = "|" + lista[i] + (30 - len(lista[i])) * " "
                środek_lista = środek_lista + środek
                i += 1
            print(góra * długość_listy + "+")
            print(środek_lista + "|")
            print(dół * długość_listy + "+")
        if wersja == "M":  # wersja z matrycą dla list zagnieżdżonych
            lista = [["opis komórki 00",'opis komóki 01'],
                     ["opis komórki 10",'opis komóki 11'],
                     ["opis komórki 20",'opis komóki 21']]
            góra = "+" + 30 * "-"
            ilość_kolumn = 2
            środek_lista = ""
            dół = "+" + 30 * "-"
            ilość_wierszy = 2
            i = 0
            j = 0
            for i, j in lista:
                środek = lista[i][i]
                print(środek)
                # środek_lista = środek_lista + środek

                # if len(lista[i]) > 30:
                #     środek = "|" + lista[i][:27] + "..."
                # else:
                #     środek = "|" + lista[i] + (30 - len(lista[i])) * " "
                # środek_lista = środek_lista + środek
                # i += 1
            print(góra * ilość_kolumn + "+")
            print(środek_lista + "|")
            print(dół * ilość_wierszy + "+")
            # i = 0
            # długość_listy = len(lista)
            # góra = "+" + 30 * "-"
            # środek = (30 - len(lista[i])) * " "
            # dół = "+" + 30 * "-"
            # print(góra * długość_listy)
            # print("|" + f"{środek}|".join(i for i in lista) + "|")
            # print(dół * długość_listy)

        jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

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

print(f"\n".join(i for i in lista_programów) +"\n") #rozdzielam elementy listy nową linią i kończę pustą linią

zapytaj_ponownie = "T"

while zapytaj_ponownie == "T":

    wybór = input("Twój wybór: ")
    if wybór.isalpha():
        wybór_litera = wybór.upper()
        if wybór_litera == "R":
            from random import randint
            x = randint(0, 9)
            info = f"Wybrałeś losowy wybór programu. Przejdziesz teraz do punktu {x}"
            #i co dalej?
        elif wybór_litera == "X":
            info = "Koniec. Dzięki, że tu zajrzałeś 😉"
            break
        else:
            info = "Twój wybór jest niepoprawny"
        print(info)
    if wybór.isdigit():
        wybór_liczba = int(wybór)
        if wybór_liczba == 1:
            rysowanie_prostokąta()
        elif wybór_liczba == 2:
            rysowanie_piramidy()
        elif wybór_liczba == 3:
            kalkulator_Celsjusz_Fahenheit()
        elif wybór_liczba == 4:
            kalkulator_Fahenheit_Celsjusz()
        elif wybór_liczba == 5:
            cyfra_pierwsza_ostatnia()
        elif wybór_liczba == 6:
            binara_na_dziesiętną()
        elif wybór_liczba == 7:
            rok_przestępny()
        elif wybór_liczba == 8:
            kalkulator_piskie_lata()
        elif wybór_liczba == 9:
            odczyty_temperatury()
        elif wybór_liczba == 10:
            rozmieniarka_pieniędzy()
        elif wybór_liczba == 11:
            rysowanie_listy()

    zapytaj_ponownie = input("\nCzy chcesz uruchomić inny program? [T/N]").upper()