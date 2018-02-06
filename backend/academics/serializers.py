from rest_framework import serializers
from academics.models import *


class NoticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notice
        fields = ('title', 'link', 'date')
