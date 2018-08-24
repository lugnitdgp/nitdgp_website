from rest_framework import serializers
from .models import *

class JournalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Journal
        fields = ('citation', 'journal', 'year')


class ConferenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conference
        fields = ('citation', 'location', 'year')


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', 'file', 'url')


class PatentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patent
        fields = ('title', 'file')
