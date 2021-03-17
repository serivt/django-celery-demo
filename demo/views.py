from rest_framework import generics, viewsets

from demo.models import CountPrimeNumbers
from demo.serializers import CountPrimeNumbersSerializer


class CountPrimeNumbersView(generics.ListCreateAPIView, viewsets.ViewSet):
    serializer_class = CountPrimeNumbersSerializer
    queryset = CountPrimeNumbers.objects.all()
