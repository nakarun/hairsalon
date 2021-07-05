from rest_framework import serializers

from hairsalon.models import News
from pointcard.models import PointCard


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ['id', 'title', 'body', 'published']


class PointCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = PointCard
        fields = '__all__'