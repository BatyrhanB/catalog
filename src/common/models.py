import uuid
import pytz
from datetime import date, time

from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


tz = pytz.timezone(settings.TIME_ZONE)


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name=_("ID"),
    )
    is_deleted = models.BooleanField(default=False, verbose_name=_("удаленный?"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("дата создания"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("дата изменения"))

    def get_date(self) -> date:
        return self.created_at.astimezone(tz).date()

    def get_hour(self) -> time:
        return self.created_at.astimezone(tz).time()

    class Meta:
        abstract = True
