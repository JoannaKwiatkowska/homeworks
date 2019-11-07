# print("składanie tekstu ze zmiennych")
# wiek = input("ile masz lat? ") # albo po prostu wiek=2
# zwierzaki = input("ile masz kotów? ") # albo po prostu zwierzaki=5
#
# zdanie= "Ala ma 2 lata i posiada 5 kotów"
# print(zdanie)
# zdanie = "Ala ma " + str(wiek) + " lata i posiada " + str(zwierzaki) + " kotów"  # pamiętaj o określeniu z jakim typem danych mamy do czynienia
# print(zdanie)
# zdanie= f"Ala ma {wiek} lata i posiada {zwierzaki} kotów"  # tutaj nie trzeba określać typu danych
# print(zdanie)
# zdanie= "Ala ma {} lata i posiada {} kotów".format(wiek,zwierzaki) # tutaj nie trzeba określać typu danych
# print(zdanie)
# zdanie= "Ala ma {a} lata i posiada {b} kotów".format(a=wiek,b=zwierzaki) # tutaj nie trzeba określać typu danych
#                                                                          # kolejność parmetrów jest dowolna
# print(zdanie)
# print("koniec zadania na składanie tekstu")

# print("sposoby wyświetlania liczb")
# liczba = 1.299
#
# print("liczba: %s" % liczba) # dokładne odwzorowanie liczby
# print("liczba: %f" % liczba) # pokazanie liczby jako float
# print("liczba: %0.1f" % liczba) # zaokrągnienie liczby do 1 miejsca po przecinku
# print("liczba: %0.3f" % liczba) # zaokrąglenie liczby do 3 miejsc po przecinku
# print("liczba: %d" % liczba) # zaokrąglenie liczby do całkowitej
# print("koniec zadania na wyświetlanie liczba")
#
# print("indeksowanie - zabawa w kolejność")
# #         012345678901
# #         123456789012
# zdanie = "encyklopedia"
# print(zdanie[4]) # ponieważ liczymy od 0 to 4 indeks to 5 znak, czyli k
# print(zdanie[-3]) # 3 znk od końca, czyli d
# print(zdanie[2:8]) # z lewej strony indeks tak, z prawej nie, czyli od 2 do 7 indeksu, czyli od 3 do 8 znaku
# print(zdanie[:7]) # od początku do 6 indeksu włącznie, czyli do 7 znaku
# print(zdanie[8:]) # od 7 indeksu do końca, czyli od 8 znaku do końca
# print(zdanie[1:7:2]) # od 1 indeksu do 6 włącznie, czyli od 2 znaku do 7, ale co drugi
# print(zdanie[::-1]) #od początku do końca, co 1 od końca
# print(zdanie[7:1:-2]) # od 8 znaku do 3, ale co drugi od początku


# print("przykłady z if")
#
# print ("Sprawdzene czy 1 równa się 1")
# if "1" == "1": # 1=1 to przypadek kiedy prawda
#    print("1 równa się 1")
# print("Koniec")

# print ("Sprwdzenie czy 1 równa się 2")
# if "1" == "2": # 1=2 to przypadek fałszu
#    print("Prawda")
# print("1 nie równa się 2 - weź sie ogarnij")

# print ("Sprawdzenie czy zmienna jest pusta")
# zmienna= None #zmienna ma wartość null
# if zmienna is None:
#    print("Zmienna jest pusta")
# print("Koniec")

# print ("Sprawdzenie czy 1 a '1' to jest to samo")
# if 1 == "1":
#    print("Prawda")
# print("1 a '1' to nie to samo, bo to są dwa różne typy danych - jedno to liczba a drugie tekst")

# print ("Sprawdzenie czy 1 a '1' to jest to samo, ale dodając wynik jeżeli fałsz")
# if 1 == "1": #przypadek fałszu bo sa dwa rozne typy danych: liczba i tekst
#    print("Prawda")
# else:
#    print("Bzdura - to są dwa różne typy danych")
# print("Koniec sprawdzenia")


# print ("Sprawdzenie parzystości liczb")
# liczba=int(input("Podaj liczbę: "))
# if liczba % 2 == 0: # znak % podaje resztę z dzielenia
#    print("Podana liczba jest parzysta, bo dzieli się przez 2 bez reszty")
# else:
#    print("Podana liczba jest nieparzysta, bo dzielenie przez dwa daje resztę")
# print("Dzięki")


#sprawdzenie czy liczba jest podzielna przez 3, przez 5 oraz przez 3 i 5 oraz nie jest podzielna przez 3 i 5
# print ("Sprawdzenie podzielności liczb przez 3 i 5")
# liczba=int(input("Podaj liczbę: ")) # int() zapewnia że wpis będzie przekonwertowany na liczbę całkowitą
# if liczba % 3 == 0 and liczba % 5 == 0: # znak % podaje resztę z dzielenia w tym przypdku przez 3 i przez 5
#     print("Podana liczba jest podzielna przez 3 i 5")
# elif liczba % 3 == 0 or liczba % 5 == 0: # elif to skrót pythona od else if
#     print("Podana liczba jest podzielna przez 3 lub 5")
#
# if liczba % 3 == 0:
#     print("Podana liczba jest podzielna przez 3")
# elif liczba % 5 == 0:
#     print("Podana liczba jest podzielna przez 5")
# else:
#     print("Podana liczba nie jest podzielna przez 3 ani przez 5")
# print("Dzięki")


# print("zabawa z wyrazami")
# wyrazy = ["raz", "dwa", "trzy"]
# wyrazy[0] = "jeden" # wyraz "jeden" zastępuje słowo o indkesie 0, czyli pierwsze, czyli "raz"
# print(wyrazy)

# print("jakieś przykłady na range")
# #range jest funkcją, która zajmuje dużo mniej miejsca w pamięci niż lista, bo podaje po kolei wartości
# liczby_parzyste = range(0,20,2) # od zera do 20 co dwa
# print(liczby_parzyste)
#
# print("teraz sprawdzam, czy liczba 2 jest parzysta")
# if 2 in liczby_parzyste:
#     print("Prawda liczba jest parzysta")
# else:
#     print("Podana liczba nie jest parzysta")
#
# print("teraz sprawdzam, czy liczba 3 jest parzysta")
# if 3 in liczby_parzyste:
#     print("Prawda liczba jest parzysta")
# else:
#     print("Podana liczba nie jest parzysta")

#print("przykład list")

# print("lista liczb od 0 do 20 - ale pokaż tylko parzyste")
# lista_liczb_parzystych = list(range(0,20,2)) #zawartością listy są liczby w zadanym zakresie
# print(lista_liczb_parzystych) #graficzna prezentacja listy
# lista_liczb_parzystych = tuple(range(0,20,2)) #tuple róznią się od listy nawiasami - lista jest w [], a tuple w ()
# print(lista_liczb_parzystych) #graficzna prezentacja tuple

# print("przykład list")
# lista6 = list("pierwszy") # wyraz zostanie podzielony na literki - iterowanie elementu
# print(lista6)
#
# lista7 = ["pierwszy"] # wyraz zostanie wziety jako całość
# print(lista7)
#
# lista8 = ["p","i","e","r","w","s","z","y"] # tutaj dzieje się to samo co w przypadku listy6
# print(lista8)

# napis = "dwa"
# lista = list(napis) # wyraz zostanie podzielony na literki
# print(lista)
# lista[0] = 'a' # w wyrazie zostanie podmieniona pierwsza literka na 'a'
# print(lista)

# zakupy = ["kielbasa","piwko","chipsy","wegiel","kubeczki"]
# print(zakupy)
# zakupy.append("talerzyki") #dodawanie do juz istniejacej listy na koniec
# print(zakupy)
# zakupy.insert(0,"grill") #dodanie grilla na poczatku listy
# print(zakupy)
# zakupy[0]='elektryczny grill' #zamiana grilla na elektrycznego grilla
# print(zakupy)
# zakupy.remove("piwko") #usuwanie piwka, nie trzeba wiedziec na ktorej pozycji jest piwko, po prostu ma je usunac
# print(zakupy)
# if "vodka" in zakupy: #żeby nie wywalił się błąd - najpierw sprawdzenie czy "vodka" jest na liście - idiotoodporność
#     zakupy.remove("vodka")
# print(zakupy)
# del(zakupy[0]) #usuń pierwszą pozycję z listy
# print(zakupy)
# zakupy.sort() #sortowanie alfabetyczne od początku
# print(zakupy)
# zakupy.sort(reverse=True) #sortowanie alfabetyczne od końca
# print(zakupy)

# print("Listy w listach")
# lista = [[1,2,3],[4,5,6],[7,8,9]]
# # lista = (
# #             [1,2,3],
# #             [4,5,6],
# #             [7,8,9]
# # )
# print(lista)
#
# liczba = lista[1][2] #znajdowanie pozycji w listach - druga lista [1] i trzecia pozycja [2]
# print(liczba)

# print("zadania na pętle - przykład na spelnianie warunku jeżeli jest prawdą")
# print("Start")
#
# zapytaj_ponownie = "T"
#
# while zapytaj_ponownie == "T":
#     print("Jestem w pętli")
#     zapytaj_ponownie=input("Czy zapytać ponownie? [T/N]").upper() #upper zamienia na duże litery - zabezpieczenie przed małymi literami
#     # zapytaj_ponownie=input("Czy zapytać ponownie? [T/N]") #to samo co powyżej ale w innej konwencji
#     # zapytaj_ponownie=zapytaj_ponownie.upper()
#     print("Odpwiedziałeś: " + zapytaj_ponownie)
#
# print("Koniec")

# print("przykład dla for")
#
# zakupy= ["kielbasa","piwko","chipsy","wegiel","kubeczki"]
# print(zakupy)
# for przedmiot in zakupy:
#     if przedmiot == "piwko":
#         znak = '[x] '
#     else:
#         znak = '[ ] '
#     print(znak + przedmiot)
