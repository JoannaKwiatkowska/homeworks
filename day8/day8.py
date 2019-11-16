# wyjątki
# try:
#     raise RuntimeError("Ooops!")
# except RuntimeError:
#     print("Coś")
# else:
#     print("Coś")
# finally:
#     print("Zawsze się wykonam :) ")

# debbuger
# days = ['poniedzialek', 'wtorek', 'sroda', 'czwartek', 'piatek', 'sobota', 'niedziela']
# weekend = ('sobota', 'niedziela')
#
# for day in days:
#     if day in weekend:
#         print("Jest weekend")
#     else:
#         print("Trzeba pracowac")


# zdjęcia
# from PIL import Image
# image = Image.open('lesio.jpg')  # otworzenie obrazka, który jest w tym samym pliku

# image : Image.Image = Image.open('lesio.jpg')  # taki zapis gdyby pycharm nie chciał podpowiadać metod i funkcji
# print(type(image))  # sprawdzenie typu zmiennej

# image.show()  # wyświetlenie zdjęcia w domyślnej przeglądarce

# image = image.resize((64, 64))  # zmiana rozmiaru zdjęcia
# image = image.rotate(180)  # obrót o 180 stopni
# image.save('lesio_resize.jpg')  # zapis zdjęcia pod nową nazwą

# moduł do wykonywania zapytań do zasobów internetowych
# import requests
# api_key = '800101cc05e0bcd5b88c816246c988ff'
# api_host = 'http://api.openweathermap.org/data/2.5/weather'
# city = 'Gdansk'
#
# result = requests.get(f"{api_host}?appid={api_key}&q={city}")
#
# dict = result.json()  # utworzenie słownika
#
# print(f"temperatura: {dict['main']['temp']}")
# print(f"wiatr: {dict['wind']['speed']} m.s")
# pass

# from bs4 import BeautifulSoup  # parsowanie
# import requests
#
# page = requests.get('https://wallpaperlist.com/')  # sciagniecie całę strony
# parser = BeautifulSoup(page.content, 'html.parser')  # budujemy parsa
# images = parser.find_all('img')  # metoda szukania wszystkich obiektów img
# for image in images:  # każdy element listy to osobne zdjęcie
#     print(image['src'])  # src to znacznik w htmlu
#     # do ścianiętych adresó trzebaby dodać adres domeny: https://wallpaperlist.com/
#     # przykład: https://wallpaperlist.com/uploads/wallpaper/thumb/blu/blue-blue-sea-ocean-wallpaper-59be9a8b72a6b.jpg

