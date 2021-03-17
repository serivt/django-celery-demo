from django_celery_results.models import TaskResult
from rest_framework import generics, viewsets

from demo.models import CountPrimeNumbers
from demo.serializers import CountPrimeNumbersSerializer, TaskResultSerializer


class CountPrimeNumbersView(generics.ListCreateAPIView, viewsets.ViewSet):
    serializer_class = CountPrimeNumbersSerializer
    queryset = CountPrimeNumbers.objects.all()


class TaskResultView(generics.ListAPIView, viewsets.ViewSet):
    serializer_class = TaskResultSerializer
    queryset = TaskResult.objects.all()
