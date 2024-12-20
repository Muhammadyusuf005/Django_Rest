from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from myapp.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class AccountCreateSerializer(serializers.ModelSerializer):
    """
    This class is used to change json format when creating or update new account
    """
    class Meta:
        model = Account
        fields = '__all__'

    def create(self, validated_data):
        """
        This method is used for hashing password when creating new account!
        """
        validated_data['password'] = make_password(validated_data['password'])
        return super(AccountCreateSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        """
        This method is used for hashing password when creating new account!
        """
        if instance.password != validated_data['password']:
            validated_data['password'] = make_password(validated_data['password'])
        return super(AccountCreateSerializer, self).update(instance, validated_data)


