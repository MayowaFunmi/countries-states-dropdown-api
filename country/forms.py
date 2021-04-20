from django import forms
from .models import Country, Person, City, LocalGovernmentDropdown, LocalGovernmentArea
import pycountry

# get country list
countries = list(pycountry.countries)

country_name = []
country_code = []
country_list = [] # add to widgets

for country in countries:
    country_name.append(country.name)
    country_code.append(country.alpha_2)

country_list.extend(a for a in zip(country_code, country_name))


# get state list

cities = list(pycountry.subdivisions)

subs = pycountry.subdivisions.get(country_code='ZW')

sub_name = []
sub_code = []
div_list = []   # add to widgets

for sub in subs:
    sub_name.append(sub.name)
    sub_code.append(sub.country_code)

# div_list.append([list(x) for x in zip(sub_code, sub_name)])
div_list.extend(x for x in zip(sub_code, sub_name))


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['birthdate', 'country', 'city']
        #widgets = {'country': forms.Select(choices=country_list),'city': forms.Select(choices=div_list)}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')


class LocalGovtForm(forms.ModelForm):
    class Meta:
        model = LocalGovernmentDropdown
        fields = ['state', 'local_govt_area']
        #widgets = {'country': forms.Select(choices=country_list),'city': forms.Select(choices=div_list)}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['local_govt_area'].queryset = LocalGovernmentArea.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['local_govt_area'].queryset = LocalGovernmentArea.objects.filter(state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['local_govt_area'].queryset = self.instance.state.localgovernmentarea_set.order_by('name')
