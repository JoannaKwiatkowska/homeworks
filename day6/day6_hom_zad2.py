# 2) Napisz/dokończ program z zajęć "Księga gości". Program oparty o dowolny format pliku (csv, pickle, własny).
#   Program powinien mieć mini menu z odtępnymi funkcjami:
#   A) dodawanie nowego wpisu
#   B) wyszukiwanie wpisów po treści
#   C) wyświetlanie wszystkich wpisów od najstarszych
#   D) wyświetlanie wszystkich wpisów od najmłodszych
#   E) wyświetlanie pojedynczych wpisów, N - następny, P - poprzedni
#   F) wyświetlanie losowowego wpisu
#   X) wyjście z programu

import csv
import datetime
from operator import itemgetter
from random import randint


def dodaj_wpis():
    with open('KsięgaGości.csv', 'a+', newline='', encoding='utf-8') as ksiega:
        csv_write = csv.writer(ksiega)
        imie = input("Podaj imię: ")
        nazwisko = input("Podaj nazwisko: ")
        miejscowosc = input("Podaj miejscowość: ")
        telefon = input("Podaj telefon: ")
        wiek = input("Podaj wiek: ")
        data = datetime.datetime.now()
        # csv_write.writerow(['imie', 'nazwisko', 'miejscowosc', 'telefon', 'wiek', 'data'])  # nagłówki kolumn
        nowy_wpis = [imie, nazwisko, miejscowosc, telefon, wiek, data]
        print(nowy_wpis)
        csv_write.writerow(nowy_wpis)
        # pokaż ile jest już wisów
        ksiega.seek(0)
        linia = 0
        for wiersz in ksiega:  # pobieranie kolejnych linii z pliku
            linia += 1
        ile_wpisow = linia - 1  # odliczenie nagłówka
        print(f"Wpisów jest: {ile_wpisow}.")


def wyszukaj_wpis():
    with open('KsięgaGości.csv', 'a+', newline='') as ksiega:
        ksiega.seek(0)  # ustawianie kursora na początku
        reader = csv.reader(ksiega)
        wpisy = list(reader)
        jeszcze_raz = "T"
        while jeszcze_raz == "T":
            kolumna = input("Chcesz wyszukiwać po imieniu (I), nazwisku (N), miejscowośći (M), "
                            "telefonie (T), wieku (W)?").upper()
            znajdz = input("Napisz czego mam dokładnie szukać? ")

            ile_jest = 0
            linia = 0
            for wiersz in wpisy:  # sprawdzanie kolejnych linii
                if kolumna == "I" and wiersz[0] == znajdz \
                        or kolumna == "N" and wiersz[1] == znajdz \
                        or kolumna == "M" and wiersz[2] == znajdz \
                        or kolumna == "T" and wiersz[3] == znajdz \
                        or kolumna == "W" and wiersz[4] == znajdz:
                    print(wiersz)
                    ile_jest += 1
                linia += 1
            ile_wpisow = linia - 1  # odliczenie nagłówka
            print(f"Szukana fraza została znaleziona: {ile_jest} wierszach, "
                  f"a {ile_wpisow - ile_jest} wierszy nie zawiera tej frazy.")
            jeszcze_raz = input("Czy chcesz wyszukiwać po innej kolumnie? T/N").upper()


def wyswietl_asc():
    with open('KsięgaGości.csv', 'a+', newline='') as ksiega:
        ksiega.seek(0)  # ustawianie kursora na początku
        reader = csv.reader(ksiega)
        wpisy = list(reader)
        kolumna = input("Wybierz po której kolumnie chcesz sortować: imię (I), nazwisko (N), miejscowość (M), "
                        "telefon (T), wiek (W), data (D)?").upper()
        if kolumna not in ("I", "N", "M", "T", "W", "D"):
            print("Wybrłeś literę poza listy, więc posortuję wg kolejności wpisów")
            sortowana_kolumna = 5
        elif kolumna == "I":
            sortowana_kolumna = 0
        elif kolumna == "N":
            sortowana_kolumna = 1
        elif kolumna == "M":
            sortowana_kolumna = 2
        elif kolumna == "T":
            sortowana_kolumna = 3
        elif kolumna == "W":
            sortowana_kolumna = 4
        elif kolumna == "D":
            sortowana_kolumna = 5
        nowa_lista = wpisy[1:]  # pominąć nagłówek ponieważ sortowanie wrzuci go na koniec
        nowa_lista.sort(key=itemgetter(sortowana_kolumna))
        print(wpisy[0])  # wyświetlenie nagłówków
        licznik = 0
        for wpis in nowa_lista:
            print(nowa_lista[licznik])
            licznik += 1


def wyswietl_desc():
    with open('KsięgaGości.csv', 'a+', newline='') as ksiega:
        ksiega.seek(0)  # ustawianie kursora na początku
        reader = csv.reader(ksiega)
        wpisy = list(reader)
        kolumna = input("Wybierz po której kolumnie chcesz sortować: imię (I), nazwisko (N), miejscowość (M), "
                        "telefon (T), wiek (W), data (D)?").upper()
        if kolumna not in ("I", "N", "M", "T", "W", "D"):
            print("Wybrłeś literę poza listy, więc posortuję wg kolejności wpisów")
            sortowana_kolumna = 5
        elif kolumna == "I":
            sortowana_kolumna = 0
        elif kolumna == "N":
            sortowana_kolumna = 1
        elif kolumna == "M":
            sortowana_kolumna = 2
        elif kolumna == "T":
            sortowana_kolumna = 3
        elif kolumna == "W":
            sortowana_kolumna = 4
        elif kolumna == "D":
            sortowana_kolumna = 5
        nowa_lista = wpisy[1:]  # pominąć nagłówek ponieważ sortowanie wrzuci go na koniec
        nowa_lista.sort(key=itemgetter(sortowana_kolumna), reverse=True)
        print(wpisy[0])  # wyświetlenie nagłówków
        licznik = 0
        for wpis in nowa_lista:
            print(nowa_lista[licznik])
            licznik += 1


def wyswietl_wpis():
    with open('KsięgaGości.csv', 'a+', newline='') as ksiega:
        ksiega.seek(0)  # ustawianie kursora na początku
        reader = csv.reader(ksiega)
        wpisy = list(reader)
        ilosc_wpisow = len(wpisy) - 2
        jeszcze_raz = "T"
        while jeszcze_raz == "T":
            wpis = input("Który wpis wyświetlić? ")
            if wpis.isdigit() is False or int(wpis) > ilosc_wpisow:
                print(f"Wpisz cyfrę i to nie większą niż {ilosc_wpisow}!")
                jeszcze_raz = "T"
            elif wpis.isdigit() is True:
                wpis = int(wpis)
                # wyświetlanie nagłówka i wybranej pozycji
                print(wpisy[0])
                print(wpisy[wpis + 1])

                wpis_kolejny = "N"
                while wpis_kolejny in ("N", "P"):
                    wpis_kolejny = input("Wyświetlić następny (N) czy poprzedni (P) wpis? N/P\n"
                                         "Każda inna litera to wyjście z programu.").upper()
                    # pozycja następna
                    if wpis_kolejny == "N" and int(wpis) < ilosc_wpisow:
                        wpis = wpis + 1
                        print(wpisy[wpis+1])
                    elif wpis_kolejny == "N" and int(wpis) >= ilosc_wpisow:
                        print("Nie ma następnej wartości - jesteś na ostatniej pozycji")
                    # pozycja poprzednia
                    elif wpis_kolejny == "P" and int(wpis) > 1:
                        wpis = wpis - 1
                        print(wpisy[wpis])
                    elif wpis_kolejny == "P" and int(wpis) == 1:
                        print("Nie ma poprzedniej wartości - jesteś na pierwszej pozycji")
                    else:
                        print("Wybrałeś wyjście z programu.")
                        jeszcze_raz = "N"
                        break
            else:
                jeszcze_raz = "N"


def losowy_wpis():
    with open('KsięgaGości.csv', 'a+', newline='') as ksiega:
        ksiega.seek(0)  # ustawianie kursora na początku
        reader = csv.reader(ksiega)
        wpisy = list(reader)
        ilosc_wpisow = len(wpisy)
        jeszcze_raz = "T"
        while jeszcze_raz == "T":
            # wyświetlanie nagłówka
            print(wpisy[0])
            # wyświetlenie losowej pozycji
            wpis = randint(1, ilosc_wpisow)  # losowy wybór wpius od 1 do tylu wierszy ile jest aktualnie w pliku
            print(wpisy[wpis + 1])
            print(f"Wyświetlony wiersz: {wpis}")
            jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()


menu = ["Witaj w Księdze Gości. Co chcesz zrobić?: ",
        "1) Dodać nowy wpis",
        "2) Wyszukać wpisy po treści",
        "3) Wyświetlić wszystkie wpisy od najstarszych",
        "4) Wyświetlić wszystkie wpisy od najmłodszych",
        "5) Wyświetlić pojedyncze wpisy",
        "6) Wyświetlić losowowy wpisu",
        "7) Wyjść z programu"]

zapytaj_ponownie = "T"
while zapytaj_ponownie == "T":
    print(f"\n".join(i for i in menu) + "\n")  # rozdzielam elementy listy nową linią i kończę pustą linią
    wybor = input("Twój wybór: ")
    if wybor.isdigit():
        wybor_liczba = int(wybor)
        if wybor_liczba == 1:
            dodaj_wpis()
        elif wybor_liczba == 2:
            wyszukaj_wpis()
        elif wybor_liczba == 3:
            wyswietl_asc()
        elif wybor_liczba == 4:
            wyswietl_desc()
        elif wybor_liczba == 5:
            wyswietl_wpis()
        elif wybor_liczba == 6:
            losowy_wpis()
        elif wybor_liczba == 7:
            info = "Wybrałeś wyjście z programu. Dzięki, że tu zajrzałeś 😉"
            print(info)
            break
        else:  # liczba poza dostępną listą
            info = "Twój wybór jest niepoprawny"
    else:  # jeżeli wybór nie jest liczbą
        info = "Twój wybór jest niepoprawny"
        print(info)
    zapytaj_ponownie = input("\nCzy chcesz uruchomić inny program? [T/N]").upper()
    info = "Koniec. Dzięki, że tu zajrzałeś 😉"
    print(info)
