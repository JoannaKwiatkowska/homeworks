
# comments #komentarz w jednej
# można jednocześnie zakomentować i odkomentować kilka linijek - zaznaczasz wszystkie i kombinacja klawiszy: Ctrl + /
# znak \ to backslash, a znak / to slash
"""comments 
in few lines
"""

# edycja configuracji Ctrl + Shift + F10

x = input("Podaj liczbę pierwszą: ")
y = input("Podaj liczbę druga: ")
suma = x + y # liczby potraktowane są jako string
print(suma)
suma = int(x) + int(y) # string zamieniony na int
print(suma)

tekst = "Tytuł: \"Ala ma kota\"" # wyświetlanie cudysłowów w środku zdania - metoda 1: znak \ przed "
print(tekst)
tekst = """Tytuł: "Ala ma kota" """ # wyświetlanie cudysłowów w środku zdania - metoda 2: potrójny znak "
print(tekst)
tekst = 'Tytuł: "Ala ma kota"' # wyświetlanie cudysłowów w środku zdania - metoda 3: użycie ' zamiast "
print(tekst)
tekst="test\test\nowy test" # w przypadku adresów w takim zapisie znaki są źle czytane: \t - tabulacja, \n - nowa linia
print(tekst)
tekst=r"test\test\nowy test" # znak r przed tekstem powoduje, że znaki specjalne nie są czytane
print(tekst)
tekst="wiele\nlinijek\ntekstu" # metoda robicia długiego tekstu na kilka linijek
print(tekst)

tekst = 'Tytuł: "Ala ma kota"'
print(tekst.upper()) # wydrukownie tesktu dużymi literami
dlugosc = len(tekst) # obliczenie ilości znaków drukowanych w zdaniu
print(dlugosc)

print(tekst[0]) # wydrukuj pierwszy znak (indeks 0)
print(tekst[3:5]) # wyrukuj znaki od 4 do 5 (indeksy 3 i 4, bo 5 indeks nie zawiera się w przedziale)
print(tekst[dlugosc-1]) # wydrukuj ostatni znak
print(tekst[-3]) # wydrukuj 3 znak od końca
print(tekst[:7]) # wydrukuj od początku do znaku 7 (indeksu 9)
print(tekst[7:]) # wydrukuj od 8 znaku do końca
print(tekst[1:7:2]) # wydrukuj od 2 do 7 znaku co drugi
print(tekst[::-1]) # wydrukuj wszystkie znaki od końca

#ulamek = 1.34
#ilosc_powtorzen = 4

#print(ilosc_powtorzen*tekst)
#print(10*"=====")

exit() # wyjście z programu