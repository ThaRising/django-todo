from rest_framework import serializers
from . import models as todo_models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo_models.Model
        fields = "__all__"
