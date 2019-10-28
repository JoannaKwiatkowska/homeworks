# 1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita i odwrotnie (wyświetlając wzór i kolejne obliczenia)
# print("zadanie 1")
#
# skala=input("Z której skali chcesz przeliczyć stopie: Fahrenheita czy Celsjusza? [F/C]")
#
# if skala.upper() == "F":
#     print("Wybrano przeliczanie z Fahrenheita na Celsjusza")
#     Fahrenheit = float(input("Podaj temperaturę w stopniach Fahrenheita: "))
#     Celsjusz_temp = round(((Fahrenheit-32)/1.8),1)
#     print(f"{Fahrenheit} stopni Fahrenheit to {Celsjusz_temp} w stopaniach Celsjusza")
#     print(f"Wzór to: (Fahrenheit-32)/1.8") #jak poadż wzór z zmiennej Celsjusz_temp?
# elif skala.upper() == "C":
#     print("Wybrano przeliczanie z Celsjusza na Fahrenheita")
#     Celsjusz = float(input("Podaj temperaturę w stopniach Celsjusza: "))
#     Fahrenheit_temp = round((32 + 1.8*Celsjusz),1)
#     print(f"{Celsjusz} stopni Celsjusza to {Fahrenheit_temp} w stopaniach Fahrenheita")
#     print(f"Wzór to: 32 + 1.8*Celsjusz") #jak poadż wzór z zmiennej Fahrenheit_temp?
# else:
#     print("Wpisłeś niepoprawną wartość")
#
# print("Koniec zadania 1")


# 2. Napisz program, który poda pierwszą i ostatnią cyfrę podanej liczby
# print("Zadanie 2")
#
# liczba=input("Podaj dwolną liczbę całkowitą: ")
#
# if liczba.isdigit()==False:
#     print(f"{liczba} to nie jest liczba całkowita")
# else:
#     print(f"Wpisano liczbę {liczba}")
#     cyfra_pierwsza=liczba[0]
#     cyfra_ostatania=liczba[-1]
#     print(f"Pierwsza cyfra to {cyfra_pierwsza}")
#     print(f"Ostatnia cyfra to {cyfra_ostatania}")
#
# print("Koniec zadania 2")


# 3. Napisz program, który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków | (bok) - (góra/dół) + (wierzchołek)
# print("Zadanie 4")
# bok_a = int(input("Podaj wymiar pierwszego boku: "))
# bok_b = int(input("Podaj wymiar drugiego boku: "))


# 4. Napisz program do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.
# print("Zadanie 4")
#
# #cyfra = int(111111)
# #cyfra = 1*0+1*2+1*4+1*8+1*16+1*32 = 63
# #cyfra[-1]*2**0 + cyfra[-2]*2**1 + cyfra[-3]*3**2 + cyfra[-4]*4**3 + cyfra[-5]*2**4 + cyfra[-6]*2**5 #zapis zaczyna się od tyłu
#
# binarna = input("Podaj liczbę binarną do przeliczenia na dziesiętną: ")
#
# licznik = int(1)
# wynik = int(binarna[-1])**0 #ostatnia liczba do potęgi zerowej 0**=0, dowolna inna liczba**0=1
# while licznik in range(1,len(binarna)):
#     dziesiętna = int(binarna[-(licznik+1)])*2**(licznik) #dlaczego 1 do potęgi 0 daje zero?
#     wynik = wynik + dziesiętna
#     licznik = licznik+1
# print(f"Liczba binarna {binarna} to liczba dziesiętna {wynik}")
#
# print("Koniec zadania 4")

# 5. Napisz program do sprawdzania czy podany rok jest rokiem przestępnym

# print("Zadanie 5")
# rok=input("Podaj rok: ")
#
# if len(rok) != 4 or rok.isdigit()==False: #sprawdza czy długość ma więcej niż 4 znaki oraz czy znaki są liczbami
#     print(f"{rok} to nie jest poprawny rok")
# elif int(rok) % 4 == 0: #rok przestęny jest podzielny przez 4
#     print(f"Rok {rok} jest przestępny")
# elif int(rok) % 100 == 0 and rok % 400 == 0: #rok przestęny jest podzielny przez 100 i 400, ale lata podzielne przez 100, ale niepodzielne przez 400 nie są przestępne.
#     print(f"Rok {rok} nie jest przestępny")
# else:
#     print(f"Rok {rok} nie jest przestępny")
#
# print("Koniec zadania 5")

# 6. Stwórz program który przyjmie w parametrze dowolną listę np ['col1', 'col2', 'col3'] i wyświetli:
#    +------+------+------+
#    | col1 | col2 | col3 |
#    +------+------+------+
#    Dodatkowym atutem będzie gdy szerokość kolumn będzie zawsze równa bez względów na zawartość, tekst wyrównany do lewej.
#    Maksymalna szerokość kolumny np 30znaków jesli tekst będzie za długi niech zawartość przycina się i kończy trzema kropkami.
#    A jeszcze większym atutem będzie gdy będzie można podać liste zagnieżdżoną i narysuje się tabela z odpowiednią ilością wierszy i kolumn :)


# 7. Program przyjmuje kwotę w parametrze i wylicza jak rozmienić to na monety: 5, 2, 1, 0.5, 0.2, 0.1 wydając ich jak najmniej.

kwota = float(input("Ile chcesz rozmienić? Możesz podać kwotę w zaokrągleniu do 10 groszy "))

moneta_5zł = (kwota//5) # znak // dzieli obcnając resztę nazywa się to floor division albo integer division
moneta_2zł = (kwota - 5*moneta_5zł)//2
moneta_1zł = (kwota - 5*moneta_5zł - 2*moneta_2zł)//1
moneta_50gr = (kwota - 5*moneta_5zł - 2*moneta_2zł - 1*moneta_1zł)//0.5
moneta_20gr = round((kwota - 5*moneta_5zł - 2*moneta_2zł - 1*moneta_1zł - 0.5*moneta_50gr),3)//0.2
moneta_10gr = round((kwota - 5*moneta_5zł - 2*moneta_2zł - 1*moneta_1zł - 0.5*moneta_50gr - 0.2*moneta_20gr),3)//0.1
if type(kwota) is float and str(kwota)[-1] == 5: # czy liczba ułamkowa jest zaokrąglona do 10 gr?
    print("Liczba nie jest zaokrąglona do 10 gr")
elif type(kwota) is float:
    print(f"Monet 5 zł: {int(moneta_5zł)}")
    print(f"Monet 2 zł: {int(moneta_2zł)}")
    print(f"Monet 1 zł: {int(moneta_1zł)}")
    print(f"Monet 0.50 gr: {int(moneta_50gr)}")
    print(f"Monet 0.20 gr: {int(moneta_20gr)}")
    print(f"Monet 0.10 gr: {int(moneta_10gr)}")





# 8. Program rysujący piramidę o określonej wysokości, np dla 3
#       #
#      ###
#     #####

# print("Zadanie 8")
# wysokość = int(input("Jak wysoka ma być piramida? "))
# for i in range(1, (wysokość+1)):
#     print(((wysokość)-i)*" " + ((i*2)-1) * "#")
# print("Koniec zadania 8")

# 9. Kalkulator do wyliczania wieku psa.
#    Przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku, przez reszte lat psi rok to 4 ludzkie lata
#    Np: 15 ludzkich lat to 73 psie lata

# print("Zadanie 9")

# lata = int(input("Ile ludzkich lat ma pies: ")) #a jak ktoś poda wiek po przecinku?
#
# if lata <= 2:
#     wiek_psa = lata*10.5
#     if lata == 1:
#         print(f"Ludzki {lata} rok to pieskie {wiek_psa} lat")
#     if lata == 2:
#         print(f"Ludzkie {lata} lata to pieskie {wiek_psa} lat")
# elif lata >= 3:
#     wiek_psa = int(2*10.5) + (lata-2)*4
#     if lata <= 4:
#         print(f"{lata} ludzkie lata to pieskie {wiek_psa} lat")
#     if lata >=5:
#         print(f"{lata} ludzkich lat to pieskie {wiek_psa} lata")
#
# print("Koniec zadania 9")

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
#
#
# Uwagi:
# - Plusem będzie jeśli program choć w minimalnym stopniu zabezpieczymy przed wprowadzaniem niepoprawnych danych
# - Kolejnym plusem będzie fajna integracja z użytkownikiem np: pytanie który "podprogram" wykonać, czy wykonać coś poraz kolejny albo czy wyjść z programu
# - Niektóre programiki można wykonać bardzo szybko (np. piramidę) za pomocą wbudowanych funkcji pythona ale jeśli ktoś zrobi to na piechotę i wymyśli jakiś algorytm też będzie super :)