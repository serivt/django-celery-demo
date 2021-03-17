from celery import shared_task

from config.celery import app
from demo.models import CountPrimeNumbers, TaskStatus
from demo.utils import is_prime


class ErrorHandler(app.Task):
    abstract = True

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        cpn = CountPrimeNumbers.objects.get(pk=args[0])
        cpn.status = TaskStatus.FAILURE
        cpn.save()
        super().on_failure(exc, task_id, args, kwargs, einfo)


@shared_task(base=ErrorHandler)
def count_prime_numbers_task(cpn_pk: int, limit: int) -> None:
    cpn = CountPrimeNumbers.objects.get(pk=cpn_pk)
    cpn.status = TaskStatus.STARTED
    cpn.save()
    if limit <= 0:
        raise Exception()
    counter = 0
    for i in range(limit):
        if is_prime(i) is True:
            counter += 1
    cpn.counter = counter
    cpn.status = TaskStatus.SUCCESS
    cpn.save()


@shared_task()
def tarea_periodica_task():
    print("Se ejecuto tarea periodica!")
