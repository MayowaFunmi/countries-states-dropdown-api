from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.decorators import api_view
from country.models import Country, City, NigeriaStates, LocalGovernmentArea
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import CountrySerializer, CitySerializer, CountryOnlySerializer, RegisterSerializer, UserSerializer, \
    NigeriaStatesSerializer, LocalGovernmentAreaSerializer


@api_view(['GET'])
def apiOverview(request):
    api_url = {
        'List': '/country_list/',
        'Register or signup': '/register/',
        'Login': '/api/token/',
        'List all countries': '/country_list/',
        'List countries and their states/provinces': '/country_states_list/',
        'List the states in Nigeria and their local govt areas': '/states_lga_api/',
    }
    return Response(api_url)


@api_view(['GET'])
def countryList(request):
    countries = Country.objects.all().order_by('id')
    serializer = CountryOnlySerializer(countries, many=True)
    return Response(serializer.data)


# user registration view
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# user list view
class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


## model viewsets
class CityApi(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (AllowAny,)


class CountryApi(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (AllowAny,)


class LocalGovernmentApi(generics.ListAPIView):
    queryset = LocalGovernmentArea.objects.all()
    serializer_class = LocalGovernmentAreaSerializer
    permission_classes = (AllowAny,)


class NigeriaStatesApi(generics.ListAPIView):
    queryset = NigeriaStates.objects.all()
    serializer_class = NigeriaStatesSerializer
    permission_classes = (AllowAny,)
