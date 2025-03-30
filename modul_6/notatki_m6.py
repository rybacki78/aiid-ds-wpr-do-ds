# obsługa plików
# plik znajduje się w tej samej lokalizacji co uruchamiany skrypt
# lub jest to np. w PyCharm ustawiony folder roboczy, w którym ten plik się znajduje
uchwyt = open("plik.txt")
# podana pełna ścieżka do pliku
uchwyt = open(r"C:\plik.txt", "r")

dane = uchwyt.read()
print(dane)
uchwyt.close()


uchwyt = open(
    r"C:\plik.txt", "r", encoding="utf-8"
)  # otworzenie ze specyficznym kodowaniem


# otwarcie tylko części pliku w bajtach
uchwyt = open("plik.txt", "r", encoding="utf-8")

while True:
    dane = uchwyt.read(1024)
    print(dane, end="")
    if not dane:
        uchwyt.close()
        break

# zapisywanie
uchwyt = open("plik2.txt", "w", encoding="utf-8")
uchwyt.write("Zapisuję do pliku.")  # musi byc strng
uchwyt.close()

# nowocześniejsza metoda niz powyższa
with open("plik.txt", "r", encoding="utf-8") as file_reader:
    for linia in file_reader:
        print(linia, end="")

# możliwość wystąpienie błedu - plik zablokowany itd
try:
    with open("plik.txt", "r", encoding="utf-8") as file_reader:
        for linia in file_reader:
            print(linia, end="")
except OSError as er:
    print(f"Wystąpił wyjątek OSError: {er}")

# json
import json
import random

# lista
lista = [[random.randint(1, 100) for n in range(10)] for k in range(10)]

with open("dane_lista.json", "w") as plik:
    json.dump(lista, plik)

with open("dane_lista.json", "r") as plik:
    x = json.load(plik)

print(x)
print(type(x))

# słownik
slownik = {f"student_{x}": x**2 for x in range(1, 11)}

with open("dane_slownik.json", "w") as plik:
    json.dump(slownik, plik)

with open("dane_slownik.json", "r") as plik:
    x = json.load(plik)

print(x)
print(type(x))

# typy inne niż list i dict nie działają out of the box
# ale można poszukać metod, które pozwalają zapisać inne struktury w
# postaci list lub słowników


class Pracownik:
    pass


p = Pracownik()
p.imie = "Adam"
p.nazwisko = "Malinowski"

# print(json.dumps(p)) # nie

# tak !
print(json.dumps(p.__dict__))  # serializacja


# csv
import csv


lista = [[random.randint(1, 100) for n in range(10)] for k in range(10)]


# tworzymy plik csv korzystając z metody writerows, która przyjmuje iterowalny
# obiekt jako argument
with open("dane_lista.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(lista)

# otwieramy zapisany wcześniej plik linia po linii
with open("dane_lista.csv", newline="") as f:
    reader = csv.reader(f)
    for wiersz in reader:
        print(wiersz)

# parametry pliku csv można dostosować
with open("dane_lista.csv", newline="") as f:
    reader = csv.reader(f, delimiter=":", quoting=csv.QUOTE_NONE)
    for wiersz in reader:
        print(wiersz)

# przykład wykorzystania DictReader oraz DictWriter

# pierwszy wiersz w pliku traktowany jako lista kluczy słownika
# którym jest każdy zwracany wiersz
with open("dane.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    for wiersz in reader:
        print(wiersz["Kraj"], wiersz["2006"])


# zapis
with open("dane_2.csv", "w", newline="") as csvfile:
    kolumny = ["Kraj", "2020"]
    writer = csv.DictWriter(csvfile, fieldnames=kolumny)

    writer.writeheader()
    writer.writerow({"Kraj": "Polska", "2020": 37987654})
    writer.writerow({"Kraj": "USA", "2020": 331002651})
