from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from country.models import Country, City, LocalGovernmentArea, NigeriaStates
from rest_framework.validators import UniqueValidator


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'password2', 'email', 'first_name', 'last_name')
        # extra_kwargs = {'first_name': {'write_only': True}, 'last_name': {'write_only': True}

    def validate(self, attrs):
        username = attrs.get('username', '')
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': "Password fields didn't match"})

        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric characters')

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# User Serializer for user list and delete user views
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # extra_kwargs = {'password': {'write_only': True, 'required': True}} # this hides password from being seen

    def create(self, validated_data):   # this creates harshed password
        user = User.objects.create_user(**validated_data)
        return user


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', ]


class CountrySerializer(serializers.ModelSerializer):
    states = CitySerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['id', 'alpha_2', 'name', 'states']


class CountryOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class LocalGovernmentAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalGovernmentArea
        fields = ['id', 'name', ]


class NigeriaStatesSerializer(serializers.ModelSerializer):
    local_govt = LocalGovernmentAreaSerializer(many=True, read_only=True)

    class Meta:
        model = NigeriaStates
        fields = ['id', 'name', 'local_govt']
