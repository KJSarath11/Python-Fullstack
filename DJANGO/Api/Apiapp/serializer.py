from rest_framework import serializers
from .models import Travel

class Tserial(serializers.ModelSerializer):
    class Meta:
        model=Travel
        fields="__all__"