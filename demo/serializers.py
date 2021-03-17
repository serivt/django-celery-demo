from rest_framework import serializers

from demo.models import CountPrimeNumbers
from demo.tasks import count_prime_numbers_task


class CountPrimeNumbersSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = CountPrimeNumbers
        fields = (
            "pk",
            "limit",
            "counter",
            "status",
        )
        read_only_fields = (
            "pk",
            "counter",
            "status",
        )

    def get_status(self, obj):
        return obj.get_status_display()

    def create(self, validated_data):
        obj = super().create(validated_data)
        count_prime_numbers_task.delay(obj.pk, obj.limit)
        return obj
