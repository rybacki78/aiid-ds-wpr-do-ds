# typ list - lista
# listy są mutowalne
# listy mogą przechowywać różne typy danych

lista  = [] # pusta lista
print(lista)
print(type(lista)) # <class 'list'>
print(len(lista)) # 0

lista.append(1) # dodanie elementu do listy
print(lista)
print(len(lista)) # 1

lista.append([1,2,3]) # dodanie listy do listy
print(lista)

print(lista[0]) # 1
print(lista[1]) # [1,2,3]
print(lista[1][1]) # 2  - dostęp do elementu wewnętrznej listy

list2 = [1,2,3,4,5,6,7,8,9,10]
list3 = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']

print(list2+list3) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']    - łączenie list

list2.extend(list3) # rozszerzenie listy list3 o listę list2
print(list2) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']  - zmienna list2 została zmodyfikowana

# metoda in-place - można modyfikować listę bez przypisywania jej do nowej zmiennej
list4 = [1,5,2,8,4,7,9,2,9,0]   # lista nieposortowana
list4.sort() # sortowanie listy
print(list4) # [0, 1, 2, 2, 4, 5, 7, 8, 9, 9]
list4.sort(reverse=True) # sortowanie listy w odwrotnej kolejności
print(list4) # [9, 9, 8, 7, 5, 4, 2, 2, 1, 0]

# list slice - wyciąganie fragmentu listy
list5 = [1,2,3,4,5,6,7,8,9,10]
print(list5[2:5]) # [3, 4, 5] - wyciągnięcie elementów od 3 do 5
print(list5[:5]) # [1, 2, 3, 4, 5] - wyciągnięcie elementów od początku do 5
print(list5[5:]) # [6, 7, 8, 9, 10] - wyciągnięcie elementów od 5 do końca
print(list5[::2]) # [1, 3, 5, 7, 9] - wyciągnięcie co drugiego elementu
print(list5[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] - wyciągnięcie listy w od odwrotnej kolejności
print(list5[2:5:2]) # [3, 5] - wyciągnięcie elementów od 3 do 5 co drugi element
list5[9:] = [11,12,13] # zamiana elementów od 9 do końca
print(list5) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13]

# rozpakowywanie listy
list6 = [1,2,3]
a,b,c = list6 # przypisanie wartości z listy do zmiennych

d, *e = list6 # przypisanie pierwszej wartości do zmiennej d, a pozostałe do listy e
print(d) # 1
print(e) # [2, 3]

list7 = [[1,2,3,4],5,6,7,8,9,10]
g, *_ = list7 # przypisanie pierwszej wartości do zmiennej g, a pozostałe do listy _
print(g) # [1, 2, 3, 4] - pierwsza wartość z listy list7    - zmienna _ jest zmienna tymczasową, która nie jest używana
del(_) # usunięcie zmiennej _ - jesli nie zrobi tego garbage collector

# typ dict - słownik
# słownik jest to zbiór par klucz-wartość
# klucze muszą być unikalne

slownik = {} # pusty słownik
slownik = dict() # pusty słownik
print(slownik)
slownik = {'klucz1': 1, 'klucz2': 2, 'klucz3': 3}
print(slownik)

print(slownik.values()) # dict_values([1, 2, 3])
print(slownik.keys()) # dict_keys(['klucz1', 'klucz2', 'klucz3'])
print(slownik.items()) # dict_items([('klucz1', 1), ('klucz2', 2), ('klucz3', 3)])

print('klucz1' in slownik.keys()) # True