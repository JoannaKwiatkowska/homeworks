#zadanie 1 - tekst ze zmiennych
# #wiek = input("ile masz lat? ")
# #zwierzaki = input("ile masz kotów? ")
#
# #wiek=2
# zwierzaki=5
#
# #zdanie= "Ala ma 2 lata i posiada 5 kotów"
# #zdanie = "Ala ma " + str(wiek) + " lata i posiada " + str(zwierzaki) + " kotów"
# #zdanie= f"Ala ma {wiek} lata i posiada {zwierzaki} kotów"
# #zdanie= "Ala ma {} lata i posiada {} kotów".format(wiek,zwierzaki)
# zdanie= "Ala ma {a} lata i posiada {b} kotów".format(a=wiek,b=zwierzaki)
# print(zdanie)
#
# liczba = 1.299
#
# print("liczba: %s" % liczba)
# print("liczba: %f" % liczba)
# print("liczba: %0.1f" % liczba)
# print("liczba: %0.2f" % liczba)
# print("liczba: %d" % liczba)

#zadanie 2
#         012345678901
#zdanie = "encyklopedia"
#print(zdanie[4]) # 5 znak
#print(zdanie[-3]) # 3 znk od końca
#print(zdanie[2:8]) # od 3 do 8 znaku
#print(zdanie[:7]) # od początku do 7 znaku
#print(zdanie[8:]) # od 9 zanku do końca - 9 znak to 8 indeks
#print(zdanie[1:7:2]) # od 2 znaku do 7, ale co drugi
#print(zdanie[::-1]) #od początku do końca, co 1 od końca
#print(zdanie[7:1:-2]) # od 8 znaku do 2, ale co drugi od końca

#zadanie 3
#print ("Start")

#if "1" == "1": #przypadek prawda
#    print("Prawda")
#print("Koniec")

#print ("Start")
#if "1" == "2": #przypadek fałszu
#    print("Prawda")
#print("Koniec")

#print ("Start")
#zmienna= None
#if zmienna:
#    print("Prawda")
#print("Koniec")

#print ("Start")
#if 1 == "1": #przypadek fałszu bo sa dwa rozne typy danych: liczba i tekst
#    print("Prawda")
#print("Koniec")

#print ("Start")
#if 1 == "1": #przypadek fałszu bo sa dwa rozne typy danych: liczba i tekst
#    print("Prawda")
#else:
#    print("Bzdura")
#print("Koniec")


#sprawdzenie czy liczba jest parzysta
# print ("Sprawdzenie parzystości liczb:")
#
# liczba=int(input("Podaj liczbę: "))
#
# if liczba % 2 == 0: # znak % podaje resztę z dzielenia
#    print("Podana liczba jest parzysta")
# else:
#    print("Podana liczba jest nieparzysta")
# print("Dzięki")


#sprawdzenie czy liczba jest podzielna przez 3, przez 5 oraz przez 3 i 5 oraz nie jest podzielna przez 3 i 5
# print ("Sprawdzenie podzielności liczb przez 3 i 5")
#
# liczba=int(input("Podaj liczbę: "))
#
# if liczba % 3 == 0 and liczba % 5 == 0: # znak % podaje resztę z dzielenia w tym przypdku przez 3
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


#zadanie 4
# wyrazy = ["raz", "dwa", "trzy"]
# wyrazy[0] = "jeden" #wyraz "jeden" zastępuje słowo "raz"
# print(wyrazy)

#zadanie na range
# liczby_parzyste = range(0,20,2) #range jest funkcją, która zajmuje dużo mniej miejsca w pamięci niż lista, bo podaje po kolei wartości
# print(liczby_parzyste)
# if 21 in liczby_parzyste: #czy liczba 21 jest w zakresie podanym powyżej
#     print("Prawda")
# else:
#     print("Fałsz")
#
# lista_liczb_parzystych = list(range(0,20,2)) #graficzna prezentacja listy
# print(lista_liczb_parzystych)
#
# lista_liczb_parzystych = tuple(range(0,20,2)) #graficzna prezentacja tuple
# print(lista_liczb_parzystych)

#zadanie na listy
# lista6 = list("pierwszy") # wyraz zostanie podzielony na literki - iterowanie elementu
# print(lista6)
#
# lista7 = ["pierwszy"] # wyraz zostanie wziety jako całość
# print(lista7)
#
# lista8 = ["p","i","e","r","w","s","z","y"] # tutaj dzieje się to samo co w przypadku listy6
# print(lista8)
#
# # napis = "dwa"
# # lista = list(napis) # wyraz zostanie podzielony na literki
# # print(lista)
# # lista[0] = 'a' # w wyrazie zostanie podmieniona pierwsza literka na 'a'
# # print(lista)

zakupy= ["kielbasa","piwko","chipsy","wegiel","kubeczki"]
print(zakupy)
# zakupy.append("talerzyki") #dodawanie do juz istniejacej listy na koniec
# print(zakupy)
# zakupy.insert(0,"grill") #dodanie grilla na poczatku listy
# print(zakupy)
# zakupy[0]='elektryczny grill' #zamiana grilla na elektrycznego grilla
# print(zakupy)
# zakupy.remove("piwko") #usuwanie piwka, nie trzeba wiedziec na ktorej pozycji jest piwko, po prostu ma je usunac
# print(zakupy)
# # if "vodka" in zakupy: #idioto odporne
# #     zakupy.remove("vodka")
# # print(zakupy)
# # del(zakupy[0]) #usuń pierwszą pozycję z listy
# # print(zakupy)
# # zakupy.sort() #sortowanie alfabetyczne od początku
# # print(zakupy)
# # zakupy.sort(reverse=True) #sortowanie alfabetyczne od końca
# # print(zakupy)

#tego nie zdazylam rozkminic o co chodzi
# lista = [[1,2,3],[4,5,6],[7,8,9]]
# lista = (
#             [1,2,3],
#             [4,5,6],
#             [7,8,9]
# )
#
# lista[1][2]
# print(lista)

#zadania na pętle - przykład na spelnianie warunku jeżeli jest prawdą
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

#przykład dla for

zakupy= ["kielbasa","piwko","chipsy","wegiel","kubeczki"]
print(zakupy)
for przedmiot in zakupy:
    if przedmiot == "piwko":
        znak = '[x] '
    else:
        znak = '[ ] '
print(znak + przedmiot)
