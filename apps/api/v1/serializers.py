from rest_framework import serializers
from apps.models import Carteira


class CarteiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carteira
        fields = '__all__'
