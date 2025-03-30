# if/elif/else

# 1 prosta wersja
liczba1 = 1
liczba2 = 2

if liczba1 > liczba2:
    print("Pierwsza liczba jest większa.")

# 2 rozbudowana wersja
liczba = input("Podaj liczbę całkowitą ")
liczba = int(liczba)

if liczba < 10:
    print("To dość mała liczba")
elif 9 < liczba < 100:  # to jest wersja skrócona warunku
    print("To już całkiem duża liczba")
else:
    print("To musi być wielka liczba")

# 3 z operatorami boolowskimi
if liczba < 10 and liczba > 15:
    print("Liczba nie jest z odpowiedniego przedziału")

# powyższy warunek można zapisać również tak
if 10 > liczba > 15:
    print("Liczba nie jest z odpowiedniego przedziału")

# możemy również sprawdzić warunek zawierania się elementu w kolekcji
zbior_dopuszczalny = [1, 3, 5, 7, 9]
if liczba not in zbior_dopuszczalny:
    print("Podana liczba nie znajduje się w zbiorze")

# 4 przykład z None

lista = []
# o co pytamy? - czy lista nie jest pusta
if lista:
    print("Prawda?")
# alternatywny lepszy zapis - mniej domysłów 
if len(lista) != 0:
    print("Lista nie jest pusta.")


# 5
# if main
# Jest również specjalne zastosowanie instrukcji if
# poniższy zapis powoduje, że kod umieszczony wewnątrz tego bloku
# zostanie uruchomiony tylko w przypadku, gdy plik zostanie
# uruchomiony bezpośrednio, tak jak w tym przypadku.
# Jeżeli plik zostanie zaimportowany, to kod nie zostanie uruchomiony

if __name__ == "__main__":
    pass

# możemy też sprawdzić jaką wartość ma zmienna specjalna __name__
print(__name__)
# instrukcja pass nie robi nic, ale jeżeli wymagany jest tutaj kod, żeby
# spełnić wymogi składniowe to możemy jej użyć



# instrukcje match/case

##
user = input('Kto chce się zalogować? (admin|user)\n')

# przykład z dopasowaniem do wartości (można zastapić if/else)
match user:
    case 'admin':
        print('Przekierowuję do panelu administratora ...')
    case 'user':
        print('Przekierowuję na stronę sklepu ...')
    case _:
        print('Błędna nazwa użytkownika!')

# przykład z rozpakowaniem sekwencji (tu listy)
command = 'remove plik.txt log.txt dane.csv'

match command.split():
    case ['show']:
        print('Wylistuj wszystkie pliki i foldery: ')
        # kod
    case ['remove', *files]:
        print('Usuwanie plików: {}'.format(files))
        # kod
    case _:
        print('Nieznane polecenie')

# output
# Usuwanie plików: ['plik.txt', 'log.txt', 'dane.csv']

# petla for oraz while

# petla for
lista = [4, 5, 6]
for index, wartosc in enumerate(lista):
    print(f'{index} -> {wartosc}')

# pętla for i słowniki
# jeżeli nie wskażemy pętli for czy chcemy iterować po kluczach czy wartościach
# to domyślnie zostaną wybrane klucze
slownik = {'imie': 'Marek', 'nazwisko': 'Kowalski', 'plec': 'mezczyzna'}
for key in slownik: # domyslnie po keys
    print(key)

for val in slownik.values():
    print(val)

for key, value in slownik.items(): # zwraca przy dict sekwencje - rozpakowanie sekwencji
    print(f'{key} -> {value}')

for key in slownik:
    print(f'{key} -> {slownik[key]}')


# pętla while
counter = 0
while True:
    counter += 1
    if counter > 10:
        break

counter = 0
while counter < 5:
    print(f'{counter} mniejsze od 5')
    counter += 1

# pętla while nadaje się dobrze w sytuacji, kiedy nie wiemy kiedy (nie
# znamy liczby iteracji) się ona zakończy, np. przy pobieraniu danych
# wejściowych w oczekiwaniu na podanie komendy równej warunkowi stopu pętli

lista = []
print('Podaj liczby całkowite, które chcesz umieścić w pętli.')
print('Wpisz "stop" aby zakończyć')
while True:
    wejscie = input()
    if wejscie == 'stop':
        break
    lista.append(int(wejscie))

print('Twoja lista -> ' + repr(lista))