from rest_framework import serializers
import collections
from information.models import *


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = ('title', 'file')


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('title', 'file')


class CareerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Career
        fields = ('title', 'file')


class TenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tender
        fields = ('title', 'file')


class TEQIPSerializer(serializers.ModelSerializer):

    class Meta:
        model = TEQIP
        fields = ('title', 'file')


class RTISerializer(serializers.ModelSerializer):

    class Meta:
        model = RTI
        fields = ('title', 'file')


class NBASerializer(serializers.ModelSerializer):

    class Meta:
        model = NBA
        fields = ('title', 'file')


class NIRFSerializer(serializers.ModelSerializer):

    class Meta:
        model = NIRF
        fields = ('title', 'file')
