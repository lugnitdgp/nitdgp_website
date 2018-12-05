from rest_framework import serializers
from academics.models import *
import collections


class NoticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notice
        fields = ('title', 'file', 'date')


class CalendarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Calendar
        fields = ('year', 'file')


class RegulationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Regulation
        fields = ('title', 'file')


class FeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fee
        fields = ('title', 'file')


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = ('title', 'file')


class AdmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admission
        fields = ('title', 'file', 'link')


class AdmissionProgrammeSerializer(serializers.ModelSerializer):

    documents = AdmissionSerializer(many=True, read_only=True)

    class Meta:
        model = AdmissionProgramme
        fields = ('name', 'documents')


class AdmissionMainSerializer(serializers.ModelSerializer):

    programmes = AdmissionProgrammeSerializer(many=True, read_only=True)

    class Meta:
        model = AdmissionDegree
        fields = ('name', 'programmes')


class ExaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examination
        fields = ('year', 'title', 'file')


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('title', 'filename')


class DocumentMainSerializer(serializers.ModelSerializer):
    def get_documents(self, obj):
        result = collections.defaultdict()
        for i in self.instance:
            try:
                result[i.type].append(
                    DocumentSerializer(i).data
                )
            except KeyError:
                result[i.type] = [
                    DocumentSerializer(i).data
                ]
        return result

    documents = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = ('documents', )


class ConvocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Convocation
        fields = '__all__'
