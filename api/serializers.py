from rest_framework import serializers
from .models import Event,Location,Schedule,Ticket,Transaction

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'eventname', 'evenstart', 'evenend')
        read_only_fields = ('create_time', 'update_time', 'record_status')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'locname', 'locmap', 'address', 'city', 'event_id')
        read_only_fields = ('create_time', 'update_time', 'record_status')

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'type', 'price', 'qty', 'event_id')
        read_only_fields = ('create_time', 'update_time', 'record_status')

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('id', 'schedulename', 'schedulestart', 'scheduleend', 'event_id')
        read_only_fields = ('create_time', 'update_time', 'record_status')

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'type', 'price', 'qty', 'event_id')
        read_only_fields = ('create_time', 'update_time', 'record_status')

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'custname', 'datetrx', 'event_id')
        read_only_fields = ('create_time', 'update_time', 'record_status')