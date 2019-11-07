# print("Referencja przy prostych listach")
# lista = [1,2,3]
# nowa_lista = lista #kopiowanie listy z odwołaniem
# kopia_listy = lista.copy() #kopiowanie listy na sztywno
# kopia_listy2 = lista[:] #druga metoda kopiowania listy n sztywno
# lista[0] = 'X'
#
# print(lista)
# print(nowa_lista)
# print(kopia_listy)
# print(kopia_listy2)

#======================================================================

# print("Referencja przy zagnieżdżonych listach")
#
# import copy
#
# lista = [1,2,3,
#          ['A','B', 'C']
# ]
#
# nowa_lista = lista #kopiowanie listy z odwołaniem
# kopia_listy = lista.copy() #kopiowanie listy na sztywno - płytkie kopiowanie
# gleboka_kopia_listy = copy.deepcopy(lista) #deepcopy jest cieższą funkcją od copy
# lista[0] = 'X' #[0] pierwszy element
# lista[3][0] = 'Y' # [3] czwarta lista i [0] pierwszy element
#
# print(lista)
# print(nowa_lista)
# print(kopia_listy) #misz masz - pierwsze 3 lisy skopiował bo są na jednym poziomie, a dla czwartej zagnieżdżonej ustawił referencję
# print(gleboka_kopia_listy)

#======================================================================

# print("Funkcje w pythonie")
# def witaj(): #tworznie funkcji - nazwanie
#     print('Cześć, jestem Twoim nowym programem.') #tworznie funkcji - zawartość
#
# witaj() #wywołanie funkcji
#
# hi = witaj #przypisanie funkcji do hi
# hi() #wywołanie funkcji przypisanej
# witaj() #wywołanie funkcji oryginalnej
#
# hi = witaj() #taki zapis to wywołanie funkcji, a nie przypisanie do hi
# print(hi) #wywołanie funkcji hi daje None, bo nic do niej nie zostało przypisane

#========================================================================

# print("Argumenty funkcji")
# def do_nothing(): # () brak argumentów, (x) jeden agrument, (x,y,z) 3 argumenty, (x, y=10) drugi ma domyślą wartość, jeżeli użytkownik nie poda
#     pass
#
# def do_nothing(x,y,imie="Ola", wiek=22):
#     pass # pass = nie rób nic, bo jeszcze nie wiem co tutaj będzie ;)
#
# do_nothing(1) #błędne bo potrzebna jest druga zmienna - jest wymagana
# do_nothing(1,2,"Iza")
# do_nothing(1,2,"Iza",22)
# do_nothing(1,2,imie="Iza", 22) #nie wykona się, bo trzeba nazwać drugi domyślny parmaetr jak nazwało się pierwszy
# do_nothing(1,2,imie="Iza",wiek=22) # trzeba nazwać drugi domyślny
# do_nothing(imie="Iza",wiek=22, x=1, y=2) #przy nazwaniu wszystkich parametrów, można podawać je w dowolnej kolejności, ale raczej tego unikamy

#========================================================================

# print("Przykład 1")
# imie = "Jola"
# def zmien_imie():
#     imie="Teresa"
#     return [imie, "Jan"]
#
# print(imie) #
# zmien_imie() #tylko wywołanie fukncji - imie w funkcji jest tylko widoczne dla funkcji
# imie = zmien_imie() #wynik funkcji przypisany do zmiennej
# print(imie) #zwrócenie wyniku funkcji


# print("Przykład 2")
# def zmien_imie(imie):
#     if imie == "Joanna":
#         return 'To twoje imie'
#     else:
#         return 'To nie jest twoje imię'
#
# print("Sprawdzenie czy mam na imie Teresa")
# imie = zmien_imie('Teresa')
# print(imie)
# print("Sprawdzenie czy mam na imie Joanna")
# imie = zmien_imie('Joanna')
# print(imie)
