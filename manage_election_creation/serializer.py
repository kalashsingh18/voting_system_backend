from rest_framework import serializers
from .models import create_election
# class Candidatesserializer(serializers.ModelSerializer):
#     class Meta:
#         model=candiates
#         fields="__all__"
class Create_elections_serializer(serializers.ModelSerializer):
    class Meta:
        model=create_election
        fields="__all__"
