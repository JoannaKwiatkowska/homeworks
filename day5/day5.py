# słownik - zamiast indeksu ma klucz - jak poniżej: imie albo pesel
# to nie jest funkcja
# mutowalny typ danych
# typ referencyjny - wskaźnik na obszar w pamięci
# klucz musi być typem niezmiennym (string, int, tuple)
# klucz jest unikalny w całym słowniku
# wartość może być dowolna i nieunikalna
# odwołujemy się po kluczu

# x = {"imie": "Lukasz", "pesel": "123456789"}
# print(x["imie"])
# osoby = {"studenci": ["Ala", "Jan", "Ania"], "wyładowcy": ["doktor", "profesor"]}
# print(osoby["studenci"][1])
# osoby["wyładowcy"].append("magister")
# print(osoby.keys)  # wylistoawnie wszystkich kluczy
# print(osoby.values)  # wylistowanie wszystkich wartości
# for key, item in osoby.items():
#     print(key, item)

# przykład 1
# tworzenie słownika
# contacts = {
#     "names": ['Ala', 'Ola', 'Jan'],
#     "surnames": ['Kowalska', 'Malinowska', 'Igrekowski'],
#     "cities": ['Gdańsk', 'Sopot', 'Gdynia']
# }

# print(contacts)  # drukuje całą listę
# print(contacts['cities'])  # drukuje tylo miasta

# contacts['cities'].append('Rumia')  # dodawanie nowego miasta na koniec listy miast
# print(contacts['cities'])  # wydruk listy miast po dodaniu Rumii

# contacts.update({'countries': ['Polska', 'USA', 'Dania']})  # dodanie nowego klucza do słownika - metoda 1
# contacts['countries'] = ['Polska', 'USA', 'Dania']  # dodanie nowego klucza do słownika - metoda 2

# print(len(contacts))  # liczy ile kluczy ma słownik
# print(contacts.keys())  # wartości kluczy - metody wbudowane w obiekt są mega zoptymalizowane, lepiej je używać
# print(list(contacts))  # wartości kluczy podane jako lista - mniej wydajne
# print(contacts.items())  # zawiera krotki

# for key, item in contacts.items():  # listuje klucze i słowniki
#     print(key, item)

# wyświetl zapis 'Ala Kowalska mieszka w Gdańsk (Polska)'
# ...

# for key, value in enumerate(contacts['names']):
#     # print(key)
#     # print(value)
#     name = value
#     surname = contacts['surnames'][key]
#     city = contacts['cities'][key]
#     country = contacts['countries'][key]
#     print(f'{name} {surname} mieszka w {city} ({country})')

# przykład 2
# contacts = [
#     {"name": 'Ala', "surname": 'Kowalska', "cities": 'Gdańsk'},
#     {"name": 'Ola', "surname": 'Malinowska', "cities": 'Sopot'},
#     {"name": 'Jan', "surname": 'Igrekowski', "cities": 'Gdynia'}
# ]
#
# print(contacts)
# # for index in range(0, len(contacts)):
# #     print(contacts[index])
#
# for rows in contacts:
#     name = rows["name"]
#     surname = rows["surname"]
#     cities = rows["cities"]
#     print(f'{name} {surname} mieszka w {cities}')

# ten sam przykład ale trochę innaczej podana lista
# contacts = {
#     "0": {"name": 'Ala', "surname": 'Kowalska', "cities": 'Gdańsk'},
#     "1": {"name": 'Ola', "surname": 'Malinowska', "cities": 'Sopot'},
#     "2": {"name": 'Jan', "surname": 'Igrekowski', "cities": 'Gdynia'}
# }
#
# for key, value in enumerate(contacts):
#     name = contacts[value]["name"]
#     surname = contacts[value]["surname"]
#     cities = contacts[value]["cities"]
#     print(f'{name} {surname} mieszka w {cities}')

# ======================================================================================================================
# otwieranie pliku: plik = open("ścieżka_do_pliku", tryb)

# ścieżka bezwzględna C://.../.../.../plik.txt
# ścieżka względna zaczyna się od nazwy katalogu np. plik.txt, folder/plik.txt,  /.../.../plik.txt
# względność oznacza miejsce w stosunku do tego gdzie jest uruchamiany program, np. nasz py

# tryby tekstowe: r - tylko odczyt, w - zapisania pliku (jednocześnie usuwa stary plik),
#                 r+ - do oczytu i zapisu, a - dopisywanie do pliku (do końca istniejacego pliku)
# "r" (czytanie),
# "w" (pisanie; kasowanie poprzedniej zawartości; utworzy plik, gdy nie istniał),
# "a" (dopisywanie; poprzednia zawartość pozostaje),
# "r+" (czytanie i pisanie; poprzednia zawartość pozostaje),
# "w+" (czytanie i pisanie; kasowanie poprzedniej zawartości),
# "a+" (czytanie i pisanie; poprzednia zawartość pozostaje),
# tryby binarne: tryby te same tylko dodajemy r, np. rb - tylko do odczytu, wb - zapisywanie do pliku

# plik.read() - odczytanie całego pliku
# plik.read([int]) - częściowe odczytywanie piku - przydatne do dużych plików
# plik.readline() - linijka
# plik.readlines() - linijki

# plik = open("śceżka_do_pliku")
# kod
# plik.close() - zamykanie pliku po użyciu żeby zwolnić je dla innych operacji

# with open("ścieżka_do_pliku") as plik:
#     #kod - dopóki jesteśmy w cięciu plik jest otwarty, od razu po wyjsciu z wcięcia python zamyka plik automatycznie

# przykład 1
# file = open('file.txt', 'w')  # otworzenie nie istniejacego pliku - uwaga trzeba dać w żeby był do modyfikacji
# file.write('Zapisz prosze do pliku')  # zapisywane tekstu do pliku
# file.close()

# przykład 2
# with open('file.txt', 'w') as file:
#     file.write('Zapisz prosze do pliku.')

# przykład 3
# with open('file.txt', 'a') as file:
#     file.write('Zapisz prosze do pliku.')

# przykład 4
# with open('file.txt', 'w') as file:
#     file.write('Zapisz prosze do pliku 1.\n')
#     print(file.tell())  # w któym miejscu piku jest ustawiony kursor
#     file.write('Zapisz prosze do pliku 2.\n')
#     print(file.tell())
#     file.write('Zapisz prosze do pliku 3.\n')
#     print(file.tell())

# przykład 5
# with open('file.txt', 'a') as file:
#     file.write('Zapisz prosze do pliku 1.\n')
#     print(file.tell())  # w któym miejscu piku jest ustawiony kursor
#     file.write('Zapisz prosze do pliku 2.\n')
#     print(file.tell())
#     file.write('Zapisz prosze do pliku 3.\n')
#     print(file.tell())

# przykład 6
# with open('file.txt', 'w') as file:
#     file.write('Zapisz prosze do pliku 1.\n')
#     file.write('Zapisz prosze do pliku 2.\n')
#     file.seek(10)  # przesunięcie kursora do 10 znaku - zaczyna nadpisywać teskt, który jest po 10 znaku
#     file.write('Zapisz prosze do pliku 3.\n')

# przykład 7 - zapis i odczyt pliku
# with open('file.txt', 'w+') as file:  # trzeba ustawić tryb w+ - czytanie i pisanie
# #     file.write('Zapisz prosze do pliku 1.\n')
# #     file.write('Zapisz prosze do pliku 2.\n')
# #     file.write('Zapisz prosze do pliku 3.\n')
# #     file.seek(0)  # trzeba to ustawić dla trybu w+ i a+ żeby kursor ustawić na poczatku
# #     print(file.read())  # czytanie odbywa się od miejsca gdzie jest kursr do końca pliku
# #     print(file.tell())  # samo czytanie pliku też przesuwa kursor
