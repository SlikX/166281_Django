from django.contrib import admin
from .models import Team, Person, Stanowisko, Osoba


# Register your models here.
# class PersonAdmin(admin.ModelAdmin):
#     # zmienna list_display przechowuje listę pól, które mają się wyświetlać w widoku listy danego modelu w panelu administracynym
#     list_display = ['imie', 'nazwisko', 'plec', 'Stanowisko', 'Data dodania']
@admin.register(Stanowisko)
class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'opis']
    # list_filter = ('nazwa')

@admin.register(Osoba)
class OsobaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'plec', 'stanowisko', 'data_dodania']
    readonly_fields = ('data_dodania',)
    list_filter = ('stanowisko', 'plec', 'data_dodania')

    @admin.display(description='Stanowisko (ID)')
    def stanowisko_with_id(self, obj):
        return f"{obj.stanowisko.nazwa} ({obj.stanowisko.id})"

admin.site.register(Team)
admin.site.register(Person)

# admin.site.register(Stanowisko)
# admin.site.register(Osoba)