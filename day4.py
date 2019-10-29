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

print("Funkcje w pythonie")
def witaj(): #tworznie funkcji - nazwanie
    print('Cześć, jestem Twoim nowym programem.') #tworznie funkcji - zawartość

witaj() #wywołanie funkcji

hi = witaj #przypisanie funkcji do hi
hi() #wywołanie funkcji przypisanej
witaj() #wywołanie funkcji oryginalnej

hi = witaj() #taki zapis to wywołanie funkcji, a nie przypisanie do hi
print(hi) #wywołanie funkcji hi daje None, bo nic do niej nie zostało przypisane
