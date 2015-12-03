from django.forms import widgets
from rest_framework import serializers
from main.models import Bracket


class BracketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bracket
        fields = ('id', 'name', 'dataJSON')