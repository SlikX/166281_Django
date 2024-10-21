# (wyświetl wszystkie obiekty modelu Osoba,)

from polls.models import Osoba
osoby = Osoba.objects.all()
print(osoby)

[# (wyświetl obiekt modelu Osoba z id = 3,)

print(Osoba.objects.get(id=3))

# (wyświetl obiekty modelu Osoba, których nazwa rozpoczyna się na wybraną przez Ciebie literę alfabetu &#40;tak, żeby był co najmniej jeden wynik&#41;,)

print(Osoba.objects.filter(imie__startswith='A'))

# (wyświetl unikalną listę stanowisk przypisanych dla modeli Osoba,)

print(Osoba.objects.values('stanowisko').distinct())

# (wyświetl nazwy stanowisk posortowane alfabetycznie malejąco,)

from polls.models import Stanowisko
print(Stanowisko.objects.order_by('-nazwa'))

# (dodaj nową instancję obiektu klasy Osoba i zapisz w bazie.)

stanowisko = Stanowisko.objects.get(id=1)
nowa_osoba = Osoba(imie='Jan', nazwisko='Kowalski', plec='1', stanowisko=stanowisko)
nowa_osoba.save()

print(nowa_osoba)

>>> # (wyświetl wszystkie obiekty modelu Osoba,)
>>> 
>>> from polls.models import Osoba
>>> osoby = Osoba.objects.all()
>>> print(osoby)
<QuerySet [<Osoba: jak 11>, <Osoba: Jan Kak>, <Osoba: jan Kar>, <Osoba: Jan Kowalski>, <Osoba: Anna Nowak>, <Osoba: Patryk Wiśniewski>, <Osoba: Adama aa>, <Osoba: Adama j>]>
>>> 
>>> [# (wyświetl obiekt modelu Osoba z id = 3,)
... 
... print(Osoba.objects.get(id=3))
... 
... # (wyświetl obiekty modelu Osoba, których nazwa rozpoczyna się na wybraną przez Ciebie literę alfabetu &#40;tak, żeby był co najmniej jeden wynik&#41;,)
... 
... print(Osoba.objects.filter(imie__startswith='A'))
  File "<console>", line 1
    [# (wyświetl obiekt modelu Osoba z id = 3,)
    ^
SyntaxError: '[' was never closed
>>> 
>>> # (wyświetl unikalną listę stanowisk przypisanych dla modeli Osoba,)
>>> 
>>> print(Osoba.objects.values('stanowisko').distinct())
<QuerySet [{'stanowisko': 1}, {'stanowisko': 1}, {'stanowisko': 2}, {'stanowisko': 1}, {'stanowisko': 3}, {'stanowisko': 4}, {'stanowisko': 2}, {'stanowisko': 1}]>
>>> 
>>> # (wyświetl nazwy stanowisk posortowane alfabetycznie malejąco,)
>>> 
>>> from polls.models import Stanowisko
>>> print(Stanowisko.objects.order_by('-nazwa'))
<QuerySet [<Stanowisko: szef>, <Stanowisko: Programista>, <Stanowisko: Kierownik>, <Stanowisko: Analityk>]>
>>> 
>>> # (dodaj nową instancję obiektu klasy Osoba i zapisz w bazie.)
>>> 
>>> stanowisko = Stanowisko.objects.get(id=1)
>>> nowa_osoba = Osoba(imie='Jan', nazwisko='Kowalski', plec='1', stanowisko=stanowisko)
>>> nowa_osoba.save()
>>> 
>>> print(nowa_osoba)
Jan Kowalski
