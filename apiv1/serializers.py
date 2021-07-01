from rest_framework import serializers

from hairsalon.models import News


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ['id', 'title', 'body', 'published']