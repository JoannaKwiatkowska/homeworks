# CSV = COMMA SEPARATED VALUES
# domyślnym znakiem rozdzielnającym jest przecinek
# cudzysłów esc drugim cudysłowiem
# csv to biblioteka do czytania csv i rozwiązuje problemy z formatowaniem
# KONSTRUKCJA I KOMENDY
# import csv
# with open('adresy.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)  # wyświetlanie zawartości
#     writer = csv.writer(csvfile)  # zapis do pliku
#     writer.writerow(['Jan', 'Kowlaski', 'Sopot', '123-432-111'])  # dopisuje do pliku

# PRZYKŁAD 1 - sumowanie wieku
# import csv
#
# imie = 0
# nazwisko = 1
# adres = 2
# telfon = 3
# wiek = 4
#
# with open('test.csv', 'r+', newline='') as csv_file:
#     csv_data = csv.reader(csv_file)
#
#     wiek_suma = 0
#
#     for row in csv_data:
#         # wiek = 4
#         if (row[4].isdigit()):  # pierwszy wiersz nie jest liczbą, bo to nazwa kolumny "wiersz", dopiero następne pozycje to liczby
#             wiek = int(row[4])  # można to sobie nazwać tak: print(row[wiek])
#             wiek_suma = wiek_suma + wiek
#     print(wiek_suma)
#
#     csv_write = csv.writer(csv_file)
#     csv_write.writerow(['Lukasz', 'Falkowicz', 'Gdansk', '365-364-635', '32'])

# PICKLE
import pickle

entries = [
    {"title": "Pierwszy wpis", "body": "Teść pierwszego wpisu", "author": "Lukasz", "date": "2019-11-07"},
    {"title": "Drugi wpis", "body": "Teść pierwszego wpisu", "author": "Lukasz", "date": "2019-11-07"}
]

# lista to typ binarny, więc musimy dać 'wb' albo 'rb+'
with open('book.pkl', 'rb+') as book_file:
    #pickle.dump(entries, book_file)
    data = pickle.load(book_file)
    print(data)

