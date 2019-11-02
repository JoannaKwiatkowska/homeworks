zapytaj_ponownie = "T"

while zapytaj_ponownie == "T":

    zadanie = input("\nKtóre zadanie chcesz obejrzeć? Wybierz liczbę od 1 do 10: ")


#1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita i odwrotnie (wyświetlając wzór i kolejne obliczenia)
    if zadanie == "1":
        print("\nWybrałeś zadanie 1")

        jeszcze_raz = "T"
        while jeszcze_raz == "T":

            skala=input("Z której skali chcesz przeliczyć stopie: Fahrenheita czy Celsjusza? [F/C]")
            if skala.upper() == "F":
                print("Wybrano przeliczanie z Fahrenheita na Celsjusza")
                Fahrenheit = input("Podaj temperaturę w stopniach Fahrenheita: ")
                if Fahrenheit.isdigit() == True: #tutaj powinno być sprawdzenie czy liczba jest float
                    Celsjusz_temp = round(((float(Fahrenheit)-32)/1.8),1)
                    print(f"{Fahrenheit} stopni Fahrenheit to {Celsjusz_temp} w stopaniach Celsjusza")
                    print(f"Wzór to: (Fahrenheit-32)/1.8") #jak poadż wzór z zmiennej Celsjusz_temp?
                else:
                    print(f"{Fahrenheit} to nie jest poprwana temperatura")
            elif skala.upper() == "C":
                print("Wybrano przeliczanie z Celsjusza na Fahrenheita")
                Celsjusz = input("Podaj temperaturę w stopniach Celsjusza: ")
                if Celsjusz.isdigit() == True: #tutaj powinno być sprawdzenie czy liczba jest float
                    Fahrenheit_temp = round((32 + 1.8*(float(Celsjusz))),1)
                    print(f"{Celsjusz} stopni Celsjusza to {Fahrenheit_temp} w stopaniach Fahrenheita")
                    print(f"Wzór to: 32 + 1.8*Celsjusz") #jak poadż wzór z zmiennej Fahrenheit_temp?
                else:
                    print(f"{Celsjusz} to nie jest poprwana temperatura")
            else:
                print("Wpisłeś niepoprawną wartość")

            print("Koniec zadania 1")

            jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()


# 2. Napisz program, który poda pierwszą i ostatnią cyfrę podanej liczby
    elif zadanie == "2":
        print("\nWybrałeś zadanie 2")

        jeszcze_raz = "T"
        while jeszcze_raz == "T":

            liczba=input("Podaj dwolną liczbę całkowitą: ")

            if liczba.isdigit()==False:
                print(f"{liczba} to nie jest liczba całkowita")
            else:
                print(f"Wpisano liczbę {liczba}")
                cyfra_pierwsza=liczba[0]
                cyfra_ostatania=liczba[-1]
                print(f"Pierwsza cyfra to {cyfra_pierwsza}")
                print(f"Ostatnia cyfra to {cyfra_ostatania}")

            print("Koniec zadania 2")

            jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()

# 3. Napisz program, który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków | (bok) - (góra/dół) + (wierzchołek)
    elif zadanie == "3":
        print("\nWybrałeś zadanie 3 (rysowanie prostokąta)")

        jeszcze_raz = "T"
        while jeszcze_raz == "T":

            bok_a = input("Podaj wymiar pierwszego boku: ")
            bok_b = input("Podaj wymiar drugiego boku: ")
            if bok_a.isdigit() == True and bok_b.isdigit() == True: #sprawdzenie czy obie liczby są poprawne
                print("+" + int(bok_a)*"-" + "+")
                for i in range(0,int(bok_b)):
                    print("|" + int(bok_a)*" " + "|")
                print("+" + int(bok_a)*"-" + "+")
            else: print("Wpisałeś coś co nie jest liczbą całkowitą")

            print("Koniec zadania 3")

            jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()


# 4. Napisz program do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.
#cyfra = int(111111)
#cyfra = 1*0+1*2+1*4+1*8+1*16+1*32 = 63
#cyfra[-1]*2**0 + cyfra[-2]*2**1 + cyfra[-3]*3**2 + cyfra[-4]*4**3 + cyfra[-5]*2**4 + cyfra[-6]*2**5 #zapis zaczyna się od tyłu
    elif zadanie == "4":
        print("\nWybrałeś zadanie 4 (Przeliczanie liczy binarnej na dziesiętną)")

        jeszcze_raz = "T"
        while jeszcze_raz == "T":

            binarna = input("Podaj liczbę binarną do przeliczenia na dziesiętną: ")
            licznik = int(1)
            wynik = int(binarna[-1]) ** 0  # ostatnia liczba do potęgi zerowej 0**=0, dowolna inna liczba**0=1
            #niebinarne = ["2","3","4","5","6","7","8","9"]
            if "2" not in list(binarna) and "3" not in list(binarna) and "4" not in list(binarna) and "5" not in list(binarna)\
                    and "6" not in list(binarna) and "7" not in list(binarna) and "8" not in list(binarna) and "9" not in list(binarna):
                    #binarna.find("1") != 0 or binarna.find("0") != 0:
                while licznik in range(1,len(binarna)):
                    dziesiętna = int(binarna[-(licznik+1)])*2**(licznik) #dlaczego 1 do potęgi 0 daje zero?
                    wynik = wynik + dziesiętna
                    licznik = licznik+1
                print(f"Liczba binarna {binarna} to liczba dziesiętna {wynik}")
            else:
                print(f"Liczba {binarna} nie jest liczbą binarną")
            #print(f"Liczba binarna {binarna} to liczba dziesiętna {wynik}")

            print("Koniec zadania 4")

            jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()


# 5. Napisz program do sprawdzania czy podany rok jest rokiem przestępnym
    elif zadanie == "5":
        print("\nWybrałeś zadanie 5 (Sprawdzanie czy rok jest przestępny)")

        jeszcze_raz = "T"
        while jeszcze_raz == "T":

            rok=input("Podaj rok do sprawdzenia: ")
            if len(rok) != 4 or rok.isdigit()==False: #sprawdza czy długość ma więcej niż 4 znaki oraz czy znaki są liczbami
                print(f"{rok} to nie jest poprawny rok")
            elif int(rok) % 4 == 0: #rok przestęny jest podzielny przez 4
                print(f"Rok {rok} jest przestępny")
            elif int(rok) % 100 == 0 and rok % 400 == 0: #rok przestęny jest podzielny przez 100 i 400, ale lata podzielne przez 100, ale niepodzielne przez 400 nie są przestępne.
                print(f"Rok {rok} nie jest przestępny")
            else:
                print(f"Rok {rok} nie jest przestępny")

            print("Koniec zadania 5")

            jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()

# 6. Stwórz program który przyjmie w parametrze dowolną listę np ['col1', 'col2', 'col3'] i wyświetli:
#    +------+------+------+
#    | col1 | col2 | col3 |
#    +------+------+------+
#    Dodatkowym atutem będzie gdy szerokość kolumn będzie zawsze równa bez względów na zawartość, tekst wyrównany do lewej.
#    Maksymalna szerokość kolumny np 30znaków jesli tekst będzie za długi niech zawartość przycina się i kończy trzema kropkami.
#    A jeszcze większym atutem będzie gdy będzie można podać liste zagnieżdżoną i narysuje się tabela z odpowiednią ilością wierszy i kolumn :)
    elif zadanie == "6":
        print("\nWybrałeś zadanie 6 (Zadanie z listą)")
        print("Upss... Nie zdążyłąm jeszcze tego zadania ogarnąć do końca ;)")

        jeszcze_raz = "T"
        while jeszcze_raz == "T":

            wersja = input("Zrobiłam dwie wersja - na kolumny lub wiersze. K/W").capitalize()
            lista = ['tutaj jest komórka 1', 'tutaj jest komórka 2', 'tutaj jest komórka 3 - ostatnia na liście']

            if  wersja == "W": #wersja na wiersze
                i = 0
                for opis in lista:
                    print("+" + 30*"-" + "+")
                    if len(lista[i])>30:
                        print("|" + lista[i][:27] + "..."+ "|")
                    else:
                        print("|" + lista[i] + (30-len(lista[i]))*" "+ "|")
                    print("+" + 30*"-" + "+")
                    i += 1
            if wersja == "K": #wersja na kolumny
                i=0
                długość_listy = len(lista)
                góra = "+" + 30*"-"
                środek = (30-len(lista[i]))*" "
                dół = "+" + 30*"-"

                print(góra*długość_listy)
                print("|" + f"{środek}|".join(i for i in lista) +"|")
                print(dół*długość_listy)

            print("Koniec zadania 6")

            jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()

# 7. Program przyjmuje kwotę w parametrze i wylicza jak rozmienić to na monety: 5, 2, 1, 0.5, 0.2, 0.1 wydając ich jak najmniej.
    elif zadanie == "7":
        print("\nWybrałeś zadanie 7 (rozmieniarka)")

        jeszcze_raz = "T"
        while jeszcze_raz == "T":

            kwota = float(input("Ile chcesz rozmienić? Możesz podać kwotę w zaokrągleniu do 10 groszy "))

            moneta_5zł = (kwota//5) # znak // dzieli obcnając resztę nazywa się to floor division albo integer division
            moneta_2zł = (kwota - 5*moneta_5zł)//2
            moneta_1zł = (kwota - 5*moneta_5zł - 2*moneta_2zł)//1
            moneta_50gr = (kwota - 5*moneta_5zł - 2*moneta_2zł - 1*moneta_1zł)//0.5
            moneta_20gr = round((kwota - 5*moneta_5zł - 2*moneta_2zł - 1*moneta_1zł - 0.5*moneta_50gr),3)//0.2
            moneta_10gr = round((kwota - 5*moneta_5zł - 2*moneta_2zł - 1*moneta_1zł - 0.5*moneta_50gr - 0.2*moneta_20gr),3)//0.1
            reszta = round((kwota - 5*moneta_5zł - 2*moneta_2zł - 1*moneta_1zł - 0.5*moneta_50gr - 0.2*moneta_20gr - 0.1*moneta_10gr),3)

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

# 8. Program rysujący piramidę o określonej wysokości, np dla 3
#       #
#      ###
#     #####
    elif zadanie == "8":
        print("\nWybrałeś zadanie 8 (rysowanie piramidy)")

        jeszcze_raz = "T"
        while jeszcze_raz == "T":

            wysokość = input("Ile pięter ma mieć piramida? ")
            if wysokość.isdigit() == True:
                wysokość = int(wysokość)
                for i in range(1, (wysokość+1)):
                    print(((wysokość)-i)*" " + ((i*2)-1) * "#")
            else:
                print(f"{wysokość} to nie jest liczba całkowita. Jakby miałabym narysować półpiętra? :)")
            print("Koniec zadania 8")

            jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()


# 9. Kalkulator do wyliczania wieku psa.
#    Przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku, przez reszte lat psi rok to 4 ludzkie lata
#    Np: 15 ludzkich lat to 73 psie lata
    elif zadanie == "9":
        print("\nWybrałeś zadanie 9 (kalkulator do wyliczania wieku psa)")

        jeszcze_raz = "T"
        while jeszcze_raz == "T":

            lata_str = input("Podaj wiek psa, ja ci przeliczę na ludzkie lata. Podaj liczbę całkowitą ")

            if lata_str.isdigit() == False:
                print(f"{lata_str} to nie jest liczba całkowita")
            else:
                lata = int(lata_str)
                if int(lata) <= 2:
                    wiek_psa = lata*10.5
                    if lata == 1:
                        print(f"Ludzki {lata} rok to pieskie {wiek_psa} lat")
                    if lata == 2:
                        print(f"Ludzkie {lata} lata to pieskie {wiek_psa} lat")
                elif int(lata) >= 3:
                    wiek_psa = int(2*10.5) + (lata-2)*4
                    if lata <= 4:
                        print(f"{lata} ludzkie lata to pieskie {wiek_psa} lat")
                    if lata >= 5:
                        print(f"{lata} ludzkich lat to pieskie {wiek_psa} lata")

            print("Koniec zadania 9")

            jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()


# 10. Zmienna dane zawiera 24 odczyty temperatury z 24 godzin. Każde 4 znaki to jeden odczyt w setnych stopni Celsjusza, tzn "2150" to 21.50°C Pomiary są dokonane o pełnych godzinach od 00:00 do 23:00. Wypisz do konsoli raport w formacie:
#
# <godzina>:<tabulator><stopnie z dokładnością do drugiego miejsca po przecinku><znak stopni>C
#
# Dla odczytów niższych niż lub równych 20°C dodaj "<tabulator>!" Dla odczytów niższych niż lub równych 18,5°C dodaj dodatkowy wykrzyknik. Nie kopiuj proszę znaku stopni. Spróbuj użyć znaku unicode \u00b0.
#
# dane = "215021482120211921002076207620502065202020152010200520002001199319901950183417501744186019462010"
# Przykład wyniku:
# (...)
# 20:00:  17.44°C    !!
# 21:00:  18.60°C    !
# 22:00:  19.46°C    !
# 23:00:  20.10°C
# (...)
    elif zadanie == "10":
        print("\nWybrałeś zadanie 10 (odczty temperatury)")

        jeszcze_raz = "T"
        while jeszcze_raz == "T":

            dane = "215021482120211921002076207620502065202020152010200520002001199319901950183417501744186019462010"

            print("(...)")
            for i in range(0,len(dane),4):
                temp = float(f"{dane[i:(i+2)]}.{dane[(i+2):(i+4)]}")
                if temp <= 18.5:
                    print(f"{int(i/4)}:00\t{temp}\u00b0C\t!!")
                elif temp <= 20:
                    print(f"{int(i/4)}:00\t{temp}\u00b0C\t!")
                else:
                    print(f"{int(i/4)}:00\t{temp}\u00b0C\t")
            print("(...)")

            print("Koniec zadania 10")

            jeszcze_raz = input("\nCzy chcesz powtórzyć? [T/N]").upper()

    else:
        print(f"\nWpisałeś {zadanie} - takiego zadania nie było do zrobienia")


    zapytaj_ponownie=input("\nCzy chcesz zobaczyć inne moje rozwiązania zadań? [T/N]").upper()

print("Dzięki, że tu zajrzałeś 😉")

# Uwagi:
# - Plusem będzie jeśli program choć w minimalnym stopniu zabezpieczymy przed wprowadzaniem niepoprawnych danych
# - Kolejnym plusem będzie fajna integracja z użytkownikiem np: pytanie który "podprogram" wykonać, czy wykonać coś poraz kolejny albo czy wyjść z programu
# - Niektóre programiki można wykonać bardzo szybko (np. piramidę) za pomocą wbudowanych funkcji pythona ale jeśli ktoś zrobi to na piechotę i wymyśli jakiś algorytm też będzie super :)



# print("Zadanie 10 - rozwiązanie z zajęć")
# dane = "215021482120211921002076207620502065202020152010200520002001199319901950183417501744186019462010"
#
# #dla ułatwienia można to sobie tak rozpisać
# dane[0:4] #0
# dane[4:8] #1
# dane[8:12] #2
# dane[12:16] #3
# dane[16:20] #4
#
# for godzina in range(0,24):
#     poczatek_zakresu = godzina * 4
#     koniec_zakresu = poczatek_zakresu + 4
#     temp = int(dane[poczatek_zakresu:koniec_zakresu]) / 100
#     tab = "" #tab można zdefinowac przez ifem, albo w else do ifa
#     if temp <= 18.5:
#         tab = "\t!"
#     elif temp <= 20:
#         tab = "\t!!"
#     # else:
#     #     tab = ""
#
#     wiersz_string = f"{godzina}:00\t {temp}\u00b0C{tab}"
#     print(wiersz_string)