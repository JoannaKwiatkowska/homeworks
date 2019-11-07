# zapis do pliku kolejnych wierszy z numerem kolejnego otwarcia pliku
with open('tekst_dopisywanie.txt', 'r+', encoding="utf8") as file:
    linia = 1
    for wiersz in file:  # pobieranie kolejnych linii z pliku
        linia += 1
    file.write(f'Ilość uruchomień: {linia}\n')
    print(f'Ilość uruchomień: {linia}\n')

# nadpisanie w pliku numeru kolejnego otwarcia pliku
with open('tekst_nadpisywanie.txt', 'a+') as file:
    file.seek(0)  # ustawienie na pierwszym znaku
    linia = file.readline()
    linia = linia[18:]  # zaczytanie fragmentu tekstu od znaku 18 do końca
    linia_int = int(linia)+1  # zamiana fragmentu tesktu na liczbę
    file.truncate(18)  # usunięcie tekstu od 18 znaku do końca
    file.write(f'{linia_int}')
    print(f'Ilość uruchomień: {linia_int}')