from . import models
from rest_framework import serializers


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Main
        fields = (
            'type', 'number', 'company', 'service'
        )

    def create(self, validated_data):
        model_fields = models.Main(**validated_data)
        model_fields.save()  # сохраняем в БД при необходимости

        return model_fields