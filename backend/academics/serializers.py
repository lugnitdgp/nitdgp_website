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


class AdmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admission
        fields = ('title', 'file')


class RegulationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Regulation
        fields = ('title', 'file')


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = ('title', 'file')


class AdmissionMainSerializer(serializers.ModelSerializer):

    def get_admission(self, obj):
        result = collections.defaultdict()
        degrees = AdmissionDegree.objects.all()
        for degree in degrees:
            programmes = degree.admissionprogramme_set.all()
            for programme in programmes:
                try:
                    result[degree.name].append({
                        programme.name: AdmissionSerializer(programme.admission_set.all(), many=True).data
                    })
                except KeyError:
                    result[degree.name] = [{
                        programme.name: AdmissionSerializer(programme.admission_set.all(), many=True).data
                    }]
        return result

    admission = serializers.SerializerMethodField()

    class Meta:
        model = Admission
        fields = ('admission', )


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
