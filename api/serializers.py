from . import models, services
from rest_framework import serializers


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Main
        fields = (
            'type', 'number', 'company', 'service'
        )

    def create(self, validated_data):
        target = services.MainServices().check_data(validated_data["number"])  # проверка данных
        validated_data["type"] = target[0]
        validated_data["company"] = target[1]
        model_fields = models.Main(**validated_data)
        model_fields.save()  # сохраняем в БД при необходимости
        return model_fields