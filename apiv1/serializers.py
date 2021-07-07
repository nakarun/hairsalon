from rest_framework import serializers

from hairsalon.models import Salon, News
from pointcard.models import PointCard, Stamp
from accounts.models import CustomerUser


class SalonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Salon
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ['id', 'title', 'body', 'published']


class PointCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = PointCard
        fields = '__all__'


class StampSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stamp
        fields = '__all__'


class CustomerUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUser
        fields = '__all__'