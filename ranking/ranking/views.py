from django.shortcuts import render
# Create your views here.
from django.contrib.auth.models import Ranking
from rest_framework import viewsets
from ranking.ranking.serializers import RankingSerializer


class RankingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Ranking.objects.all().order_by('-date_joined')
    serializer_class = RankingSerializer




