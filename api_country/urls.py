from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = 'api_country'
from . import views

#router = DefaultRouter()
#router.register('city_api/', views.CityApi)
#router.register('country_states_api/', views.CountryApi)   # list countries and states in each country
#router.register('states_lga_api/', views.NigeriaStatesApi)   # list countries and states in each country



urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    #path('api/', include(router.urls)),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('list_users/', views.UserView.as_view(), name='list_user'),
    path('country_list/', views.countryList, name='country_list'),  # list only countries and alpha_2 code
    path('country_states_list/', views.CountryApi.as_view(), name='country_states_api'),
    path('states_lga_api/', views.NigeriaStatesApi.as_view(), name='states_lga_api'),
    #path('country_state_list/<int:pk>/', views.CountryStateView.as_view(), name='country_state_list'),
]