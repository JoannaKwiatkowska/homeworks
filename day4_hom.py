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
        Celsjusz = input("Podaj temperaturę w stopniach Celsjusza: ")
        if Celsjusz.isdigit() == True:  # tutaj powinno być sprawdzenie czy liczba jest float a nie integer
            Fahrenheit_temp = round((32 + 1.8 * (float(Celsjusz))), 1)
            print(f"{Celsjusz} stopni Celsjusza to {Fahrenheit_temp} w stopaniach Fahrenheita")
            print(f"Wzór to: 32 + 1.8*Celsjusz")  # jak poadż wzór z zmiennej Fahrenheit_temp?
        else:
            print(f"{Celsjusz} to nie jest poprwana temperatura")

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
            print(f"{Fahrenheit} stopni Fahrenheit to {Celsjusz_temp} w stopaniach Celsjusza")
            print(f"Wzór to: (Fahrenheit-32)/1.8")  # jak poadż wzór z zmiennej Celsjusz_temp?
        else:
            print(f"{Fahrenheit} to nie jest poprwana temperatura")

        jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
#=======================================================================================================================
def cyfra_pierwsza_ostatnia():
    """Program, który podaje pierwszą i ostatnią cyfrę podanej liczby"""
    print("\nPrzeliczanie stopni Fahrenheita na Celsjusza")
    jeszcze_raz = "T"
    while jeszcze_raz == "T":

        liczba = input("Podaj dwolną liczbę całkowitą: ")

        if liczba.isdigit() == False:
            print(f"{liczba} to nie jest liczba całkowita")
        else:
            print(f"Wpisano liczbę {liczba}")
            cyfra_pierwsza = liczba[0]
            cyfra_ostatania = liczba[-1]
            print(f"Pierwsza cyfra to {cyfra_pierwsza}")
            print(f"Ostatnia cyfra to {cyfra_ostatania}")

        jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
#=======================================================================================================================
def binara_na_dziesiętną():
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
    """Program do sprawdzania czy podany rok jest rokiem przestępnym"""
    jeszcze_raz = "T"
    while jeszcze_raz == "T":

        rok = input("Podaj rok do sprawdzenia: ")
        if len(
                rok) != 4 or rok.isdigit() == False:  # sprawdza czy długość ma więcej niż 4 znaki oraz czy znaki są liczbami
            print(f"{rok} to nie jest poprawny rok")
        elif int(rok) % 4 == 0:  # rok przestęny jest podzielny przez 4
            print(f"Rok {rok} jest przestępny")
        elif int(
                rok) % 100 == 0 and rok % 400 == 0:  # rok przestęny jest podzielny przez 100 i 400, ale lata podzielne przez 100, ale niepodzielne przez 400 nie są przestępne.
            print(f"Rok {rok} nie jest przestępny")
        else:
            print(f"Rok {rok} nie jest przestępny")

        jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
#=======================================================================================================================
def kalkulator_piskie_lata():
    """Kalkulator do wyliczania wieku psa"""

    jeszcze_raz = "T"
    while jeszcze_raz == "T":

        lata_str = input("Podaj wiek psa, ja ci przeliczę na ludzkie lata. Podaj liczbę całkowitą ")

        if lata_str.isdigit() == False:
            print(f"{lata_str} to nie jest liczba całkowita")
        else:
            lata = int(lata_str)
            if int(lata) <= 2: # Przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku
                wiek_psa = lata * 10.5
                if lata == 1:
                    print(f"Ludzki {lata} rok to pieskie {wiek_psa} lat")
                if lata == 2:
                    print(f"Ludzkie {lata} lata to pieskie {wiek_psa} lat")
            elif int(lata) >= 3: # po drugim roku psi rok to 4 ludzkie lata
                wiek_psa = int(2 * 10.5) + (lata - 2) * 4
                if lata <= 4:
                    print(f"{lata} ludzkie lata to pieskie {wiek_psa} lat")
                if lata >= 5:
                    print(f"{lata} ludzkich lat to pieskie {wiek_psa} lata")

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
    """Program przyjmuje kwotę w parametrze i wylicza jak rozmienić to na monety: 5, 2, 1, 0.5, 0.2, 0.1 wydając ich jak najmniej."""
    jeszcze_raz = "T"
    while jeszcze_raz == "T":

        kwota = float(input("Ile chcesz rozmienić? Możesz podać kwotę w zaokrągleniu do 10 groszy "))

        moneta_5zł = (kwota // 5)  # znak // dzieli obcnając resztę nazywa się to floor division albo integer division
        moneta_2zł = (kwota - 5 * moneta_5zł) // 2
        moneta_1zł = (kwota - 5 * moneta_5zł - 2 * moneta_2zł) // 1
        moneta_50gr = (kwota - 5 * moneta_5zł - 2 * moneta_2zł - 1 * moneta_1zł) // 0.5
        moneta_20gr = round((kwota - 5 * moneta_5zł - 2 * moneta_2zł - 1 * moneta_1zł - 0.5 * moneta_50gr), 3) // 0.2
        moneta_10gr = round((kwota - 5 * moneta_5zł - 2 * moneta_2zł - 1 * moneta_1zł - 0.5 * moneta_50gr - 0.2 * moneta_20gr),3) // 0.1
        reszta = round((kwota - 5 * moneta_5zł - 2 * moneta_2zł - 1 * moneta_1zł - 0.5 * moneta_50gr - 0.2 * moneta_20gr - 0.1 * moneta_10gr),3)

        print(f"Kwotę {kwota} najlepiej rozmienić tak:")
        print(f"Monet 5 zł: {int(moneta_5zł)}")
        print(f"Monet 2 zł: {int(moneta_2zł)}")
        print(f"Monet 1 zł: {int(moneta_1zł)}")
        print(f"Monet 0.50 gr: {int(moneta_50gr)}")
        print(f"Monet 0.20 gr: {int(moneta_20gr)}")
        print(f"Monet 0.10 gr: {int(moneta_10gr)}")
        if reszta != 0:
            print(f"Nie podałeś liczby całkowitej, więc reszta {reszta} zł jest dla mnie")

        print("Koniec zadania 7")

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

        wersja = input("Zrobiłam dwie wersja - na kolumny lub wiersze. K/W").capitalize()
        lista = ['tutaj jest komórka 1', 'tutaj jest komórka 2', 'tutaj jest komórka 3 - ostatnia na liście']

        if wersja == "W":  # wersja na wiersze
            i = 0
            for opis in lista:
                print("+" + 30 * "-" + "+")
                if len(lista[i]) > 30:
                    print("|" + lista[i][:27] + "..." + "|")
                else:
                    print("|" + lista[i] + (30 - len(lista[i])) * " " + "|")
                print("+" + 30 * "-" + "+")
                i += 1
        if wersja == "K":  # wersja na kolumny
            i = 0
            długość_listy = len(lista)
            góra = "+" + 30 * "-"
            środek = (30 - len(lista[i])) * " "
            dół = "+" + 30 * "-"

            print(góra * długość_listy)
            print("|" + f"{środek}|".join(i for i in lista) + "|")
            print(dół * długość_listy)

        print("Koniec zadania 6")

        jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()
#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================
#=======================================================================================================================

lista_programów = ["Witaj w Multitool. Wybierz program który cię interesuje: ",
                  "1) Rysowanie prostokątu o zadanych parametrach",
                  "2) Rysowanie piramidy o określonej wysokości",
                  "3) Przeliczanie C->F"
                  "4) Przeliczanie C->F",
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
            print("Wybrałeś losowy wybór programu")
        elif wybór_litera == "X":
            print("Koniec. Dzięki, że tu zajrzałeś 😉")
            break
        else:
            print("Twój wybór jest niepoprawny")
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