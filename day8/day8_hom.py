# ZADANIE
# 1) ściagnij wszystkie obrazki ze strony internetowej na dysk do katalgu images
# 2) zrób miniaturki tych obrazków 64x64 i wrzuć do katalogu images/thumbs
# 3) policz ile jest zdjęć na stronie
# 4) wyślij maila z informacją ile zdjęć ściągnięto, jaki jest suaryczny rozmiar zdjęć w MB,
#    ile MB zaoszczedzilem robiac miniaturki
# 5) dopisz w mailu jaka jest pogoda w Gdańsku

import os
from bs4 import BeautifulSoup  # parsowanie
import requests
from PIL import Image
from io import BytesIO
import kalkulator_F_C
import smtplib  # import potrzebych bibiotek
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # import modulu, który będzie potrzebny do generowania @

# # utworzenie folderu images
# if os.path.exists("images"):
#     print("Katalog już istnieje!")
# else:
#     os.mkdir("images")
#     print("Katalog właśnie dodany!")
#
# # utworzenie folderu images/thumbs
# if os.path.exists("images/thumbs"):
#     print("Katalog już istnieje!")
# else:
#     os.mkdir("images/thumbs")
#     print("Katalog właśnie dodany!")
#
# # ściągnięcie zdjęć ze strony do katalogu images
# page = requests.get('https://wallpaperlist.com/')
# parser = BeautifulSoup(page.content, 'html.parser')
# images = parser.find_all('img')
#
# licznik_zdjec = 0
# inne_formaty = 0
#
# for image in images:
#     link = image['src']
#     # print(link)
#     url = f"https://wallpaperlist.com/{link}"
#     # print(url)
#     response = requests.get(url)
#     image = Image.open(BytesIO(response.content))
#     nazwa = url.split("/")
#     # print(nazwa)
#     format_pliku = url[-3:]  # 3 ostatnie litery mówią co to za format pliku - dla jpg nazwa to 9 pozycja na liście
#
#     if format_pliku == "jpg":
#         nazwa = nazwa[8]
#         # print(nazwa)
#         image.save(f"images\{nazwa}")  # zapis zdjęcia pod nową nazwą
#         image = image.resize((64, 64))  # zmiana rozmiaru zdjęcia
#         image.save(f"images\\thumbs\{nazwa}")  # zapis zdjęcia pod nową nazwą
#         licznik_zdjec = licznik_zdjec + 1
#
#     else:
#         inne_formaty = inne_formaty + 1

# sprawdzenie rozmiarów zdjęć
pliki_oryginalne = os.listdir("images")
ile_zdjec_o = 0
rozmiar_oryginal = 0
suma_rozmiar_oryginal = 0

for zdjecie in pliki_oryginalne:
    if zdjecie[-3:] == "jpg":
        rozmiar_oryginal = os.path.getsize(f"images\\{zdjecie}")
        # oryginal_KB = rozmiar_oryginal / 1024  # 1024 bajtów to jeden kilobajt
        oryginal_MB = rozmiar_oryginal / 1024 ** 2  # 1024 kilobajty to jeden megabajt
        ile_zdjec_o = ile_zdjec_o + 1
        suma_rozmiar_oryginal = suma_rozmiar_oryginal + oryginal_MB
suma_rozmiar_oryginal = "%0.2f" % suma_rozmiar_oryginal
# print(ile_zdjec_o)
# print(suma_rozmiar_oryginal)

pliki_zmniejszone = os.listdir("images\\thumbs")
rozmiar_zmniejszony = 0
suma_rozmiar_zmniejszony = 0

for zdjecie in pliki_zmniejszone:
    if zdjecie[-3:] == "jpg":
        rozmiar_zmniejszony = os.path.getsize(f"images\\thumbs\\{zdjecie}")
        oryginal_MB = rozmiar_zmniejszony / (1024 ** 2)  # 1024 kilobajty to jeden megabajt
        suma_rozmiar_zmniejszony = suma_rozmiar_zmniejszony + oryginal_MB
suma_rozmiar_zmniejszony = "%0.2f" % suma_rozmiar_zmniejszony
# print(suma_rozmiar_zmniejszony)
zaoszczedzone = float(suma_rozmiar_oryginal) - float(suma_rozmiar_zmniejszony)
# print(zaoszczedzone)

# pogoda w Gdańsku
api_key = '800101cc05e0bcd5b88c816246c988ff'
api_host = 'http://api.openweathermap.org/data/2.5/weather'
city = 'Gdansk'
result = requests.get(f"{api_host}?appid={api_key}&q={city}")
dict = result.json()  # utworzenie słownika
temperatura = dict['main']['temp']
temp_w_st_celsjusza = kalkulator_F_C.kalkulator_kelwin_celsjusz(temperatura)
pomiar = dict['dt']  # otatni pomiar - jak się do tego dostać
print(pomiar)


# wysyłka @
subject = "Ściąganie obrazków ze strony"
body = f"Pobrałam {ile_zdjec_o} zdjęć. \n" \
       f"Orgynialne zdjęcia mają {suma_rozmiar_oryginal} MB, " \
       f"a zmiejszone do rozmiaru 64x64 zajmują {suma_rozmiar_zmniejszony} MB. \n" \
       f"Zaoszczędziłam dzięki temu {zaoszczedzone} MB. \n" \
       f"Obecnie w Gdańsku jest {temp_w_st_celsjusza}°C. \n\n" \
       f"Pozdrawiam\n" \
       f"Joanna Kwiatkowska"
recipient = "joarie@wp.pl"  # wielu odbiorcóW można podawac po przecinku
mail_body = MIMEText(body)

mail = MIMEMultipart()  # utworzenie schematu, który podajemy poniżej
mail["Subject"] = subject
mail["From"] = "isapy@int.pl"  # można oś takiego: "Prezydent Polski <isapy@int.pl>"
mail["To"] = recipient
mail.attach(mail_body)

server = smtplib.SMTP("poczta.int.pl")  # adres serwera
server.starttls()  # uwierzytelnianie
server.login("isapy@int.pl", "isapython;")  # logowanie
server.send_message(mail)  # mail jest utworzony powyżej
server.quit()
