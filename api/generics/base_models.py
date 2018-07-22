from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_time = models.DateTimeField(db_column='create_time', default=timezone.now)
    update_time = models.DateTimeField(db_column='update_time', null=True)
    record_status = models.CharField(max_length=200, default='LIVE')

    class Meta:
        abstract = True
