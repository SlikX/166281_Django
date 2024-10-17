from django.contrib import admin
from .models import Team, Person, Stanowisko, Osoba


# Register your models here.
# class PersonAdmin(admin.ModelAdmin):
#     # zmienna list_display przechowuje listę pól, które mają się wyświetlać w widoku listy danego modelu w panelu administracynym
#     list_display = ['imie', 'nazwisko', 'plec', 'Stanowisko', 'Data dodania']

admin.site.register(Team)
admin.site.register(Person)

admin.site.register(Stanowisko)
admin.site.register(Osoba)