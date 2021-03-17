from django.db import models
from django.utils.translation import ugettext_lazy as _


class TaskStatus(models.IntegerChoices):
    PENDING = 0, _("Pending")
    FAILURE = 1, _("Failure")
    RECEIVED = 2, _("Received")
    STARTED = 3, _("Started")
    SUCCESS = 4, _("Success")


class CountPrimeNumbers(models.Model):
    limit = models.IntegerField(_("Limit"))
    counter = models.IntegerField(_("Counter"), default=0)
    status = models.SmallIntegerField(
        choices=TaskStatus.choices,
        default=TaskStatus.PENDING,
    )
