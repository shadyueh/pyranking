from django.contrib.auth.models import Ranking
from rest_framework import serializers


class RankingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ranking
        fields = ('url', 'name', 'score', 'round','total_time')

