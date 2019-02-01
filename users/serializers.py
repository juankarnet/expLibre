from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()  # read only
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        """
        Va a crear una instancia del objeto validated_data
        que contiene valores deserializados
        :param validated_data:
        :return:
        """
        instance = User()
        return self.update(instance,validated_data)

    def update(self, instance, validated_data):
        """
        Actualiza el contenido de un objeto instancia de usuario
        :param instance:
        :param validated_data:
        :return:
        """
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))

        instance.save()
        return instance

    def validate_username(self, data):
        users = User.objects.filter(username=data)
        if not self.instance and len(users) != 0:
            raise serializers.ValidationError("Ya existe un usuario con ese Username")
        elif self.instance and self.instance.username!=data and len(users) != 0:
            raise serializers.ValidationError("Ya existe un usuario con ese Username que quieres modificar")
        else:
            return data


