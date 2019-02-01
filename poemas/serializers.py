from rest_framework import serializers
from models import Poema

class PoemaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poema
        fields = '__all__'
        read_only_fields = ('owner',)

class PoemaListSerializer(PoemaSerializer):

    class Meta(PoemaSerializer.Meta):
        fields =('nombre','titulo', 'texto')
