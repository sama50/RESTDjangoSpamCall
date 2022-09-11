from rest_framework import serializers
from api.models import User , spanNumber
from rest_framework.permissions import IsAuthenticated

class UserRegistrationSerializer(serializers.ModelSerializer):
  # We are writing this becoz we need confirm password field in our Registratin Request
  password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
  class Meta:
    model = User
    fields=['phone', 'name', 'password', 'password2', 'email']
    extra_kwargs={
      'password':{'write_only':True}
    }

  # Validating Password and Confirm Password while Registration
  def validate(self, attrs):
    password = attrs.get('password')
    password2 = attrs.get('password2')
    if password != password2:
      raise serializers.ValidationError("Password and Confirm Password doesn't match")
    return attrs

  def create(self, validate_data):
    return User.objects.create_user(**validate_data)

class UserLoginSerializer(serializers.ModelSerializer):
  phone = serializers.CharField(max_length=255)
  class Meta:
    model = User
    fields = ['phone', 'password']

class UserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'email', 'name','phone']


class AddUserSpanSerializer(serializers.ModelSerializer):
    class Meta:
        model = spanNumber
        fields= ['number','name']

class CheckSpanSerializer(serializers.ModelSerializer):
    class Meta:
        model = spanNumber
        fields = ['number']