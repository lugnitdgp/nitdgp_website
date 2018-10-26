from rest_framework import serializers
import collections
from information.models import *


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = ('title', 'file', 'date')


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('title', 'file', 'date')


class CareerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Career
        fields = ('title', 'file', 'date')


class TenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tender
        fields = ('title', 'file', 'date')


class TEQIPSerializer(serializers.ModelSerializer):

    class Meta:
        model = TEQIP
        fields = ('title', 'file', 'date')


class RTISerializer(serializers.ModelSerializer):

    class Meta:
        model = RTI
        fields = ('title', 'file', 'date', 'link')


class NBASerializer(serializers.ModelSerializer):

    class Meta:
        model = NBA
        fields = ('title', 'file', 'date')


class NIRFSerializer(serializers.ModelSerializer):

    class Meta:
        model = NIRF
        fields = ('title', 'file', 'date')



class OfficeNoticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = OfficeNotice
        fields = ('title', 'file', 'date')


class MoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = More
        fields = ('title', 'file', 'date', 'link')


class PublicGrievanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicGrievance
        fields = ('title', 'file', 'date', 'link')


class ICCSerializer(serializers.ModelSerializer):
    class Meta:
        model = ICC
        fields = ('title', 'file', 'date', 'link')

class NADSerializer(serializers.ModelSerializer):

    class Meta:
        model = NAD
        fields = ('title', 'file', 'date')
