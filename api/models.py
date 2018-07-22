# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .generics.base_models import BaseModel
from django.utils import timezone

class Event(BaseModel):
    class Meta:
        db_table = "api_event"

    id = models.CharField(primary_key=True, max_length=255)
    eventname = models.CharField(max_length=255)
    #evenstart = models.DateTimeField(auto_now=False)
    #evenend = models.DateTimeField(auto_now=False)
    evenstart = models.CharField(max_length=255)
    evenend = models.CharField(max_length=255)

class Location(BaseModel):
    class Meta:
        db_table = "api_location"

    id = models.CharField(primary_key=True, max_length=255)
    event_id = models.IntegerField(default=100)
    locname = models.CharField(max_length=255)
    locmap = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)

class Schedule(BaseModel):
    class Meta:
        db_table = "api_schedule"

    id = models.CharField(primary_key=True, max_length=255)
    ##event = models.ForeignKey(Event, on_delete=models.CASCADE, db_column='event_id', related_name='schedule_event')
    event_id = models.IntegerField(default=100)
    schedulename = models.CharField(max_length=255)
    schedulestart = models.DateTimeField(auto_now=False)
    scheduleend = models.DateTimeField(auto_now=False)


class Ticket(BaseModel):
    class Meta:
        db_table = "api_ticket"

    id = models.CharField(primary_key=True, max_length=255)
    ##event = models.ForeignKey(Event, on_delete=models.CASCADE, db_column='event_id', related_name='ticket_event')
    event_id = models.IntegerField(default=100)
    type = models.CharField(max_length=255)
    price = models.IntegerField(default=100)
    qty = models.IntegerField(default=100)

class Transaction(BaseModel):
    class Meta:
        db_table = "api_transaction"

    id = models.CharField(primary_key=True, max_length=255)
    ##event = models.ForeignKey(Event, on_delete=models.CASCADE, db_column='event_id', related_name='trx_event')
    event_id = models.IntegerField(default=100)
    custname = models.CharField(max_length=255)
    datetrx = models.DateTimeField(default=timezone.now)