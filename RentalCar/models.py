from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class Car(models.Model):
    date_car = models.DateField()
    brand = models.CharField(max_length = 100, blank = False)
    model = models.CharField(max_length = 100, blank = False)
    currentLocation = models.CharField(max_length = 100, blank = False)
    color = models.CharField(max_length = 100, blank = True)
    purchaseDate = models.DateField()

    class Meta:
        pass

class Reservation(models.Model):
    pickUpDate = models.DateField()
    returnDate = models.DateField()
    location = models.CharField(max_length = 100, blank = False)

    class Meta:
        pass

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True, min_length = 8, allow_blank = False)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True, min_length = 8, allow_blank=False)
    first_name = serializers.CharField(max_length = 30, allow_blank = False)
    last_name = serializers.CharField(max_length = 150, allow_blank = False)

    def validate_password(self, value):
        password = value.get("password")
        password2 = value.get("password2")
        if password != password2:
            validators = [UniqueValidator(message="Password does not match")]

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password2', 'first_name', 'last_name')