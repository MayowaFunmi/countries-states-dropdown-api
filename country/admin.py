from django.contrib import admin
from .models import Country, City, Person, NigeriaStates, LocalGovernmentArea, LocalGovernmentDropdown

# Register your models here.
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Person)
admin.site.register(NigeriaStates)
admin.site.register(LocalGovernmentArea)
admin.site.register(LocalGovernmentDropdown)

admin.site.site_header = 'countries state admin'