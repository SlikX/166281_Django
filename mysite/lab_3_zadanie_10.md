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