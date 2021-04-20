from django.urls import path, include
from . import views

app_name = 'country'

urlpatterns = [
    path('add_country/', views.add_country, name='add_country'),
    path('add_city/', views.add_city, name='add_city'),
    path('country_list/', views.country_list, name='country_list'),
    #path('', views.PersonListView.as_view(), name='person_changelist'),
    path('add/', views.person_create_view, name='person_add'),
    #path('<int:pk>/', views.person_update_view, name='person_change'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),  # <-- this one here
    path('get_states/', views.country_and_state, name='get_states'),
    path('get_states_ajax/', views.country_and_state_ajax, name='get_states_ajax'),
    path('get_nigeria_states/', views.nigeria_states, name='nigeria_states'),
    path('add_local_govt_areas/', views.local_govt_areas, name='local_govt_areas'),
    path('get_states_lga_ajax/', views.get_states_lga_ajax, name='get_states_lga_ajax'),
    path('get_states_lga/', views.get_states_lga, name='get_states_lga'),

]
