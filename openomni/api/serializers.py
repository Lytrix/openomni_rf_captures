from django.contrib.gis.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse

from rest_framework import serializers
from openomni.api.models import (RawCapture,
                                 Action,
                                 )

User = get_user_model()


class ActionField(serializers.StringRelatedField):
    def to_representation(self, value):
        return ('{}-{}'.format(value.action_id, value.action))


class RawCaptureSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer to represent the Capture model """
    Description = ActionField(many=False, read_only=True, source = 'action')

    class Meta:
        model = RawCapture
        fields = '__all__'


class ActionSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer to represent the Capture model """
    class Meta:
        model = Action
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    actions = serializers.PrimaryKeyRelatedField(many=True, queryset=Action.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'actions')
