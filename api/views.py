# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets
from .models import Event,Schedule,Ticket,Transaction
from .serializers import EventSerializer, LocationSerializer, ScheduleSerializer, TicketSerializer, TransactionSerializer
from rest_framework.views import APIView, Response

class createEventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    http_method_names = ['post']

class createLocationViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = LocationSerializer
    http_method_names = ['post']

class createTicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    http_method_names = ['post']

class getEventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    http_method_names = ['get']

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class createTransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    http_method_names = ['post']

class getTransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    http_method_names = ['get']

class CustomView(APIView):
    def get(self, request, format=None):
        return Response("Some get response")
    def post(self, request, format=None):
        return Response("Some post response")