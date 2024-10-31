from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import SpyCat, Mission, Target


class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = '__all__'


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id', 'name', 'country', 'notes', 'is_complete']  # Уберите 'mission' из полей
        read_only_fields = ['mission']


class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True)

    class Meta:
        model = Mission
        fields = ['id', 'cat', 'is_complete', 'targets']

    def create(self, validated_data):
        targets_data = validated_data.pop('targets')
        mission = Mission.objects.create(**validated_data)
        for target_data in targets_data:
            # Здесь мы создаем целевые объекты, указывая, что они принадлежат созданной миссии
            Target.objects.create(mission=mission, **target_data)
        return mission

    def update(self, instance, validated_data):
        targets_data = validated_data.pop('targets', None)
        # Обновляем саму миссию
        instance.cat = validated_data.get('cat', instance.cat)
        instance.is_complete = validated_data.get('is_complete', instance.is_complete)
        instance.save()

        # Обновляем цели, если они были переданы
        if targets_data is not None:
            for target_data in targets_data:
                # Здесь можно добавить логику для обновления целей,
                # например, если нужно обновить существующие цели
                target_id = target_data.get('id', None)
                if target_id:
                    target = get_object_or_404(Target, id=target_id, mission=instance)
                    target.name = target_data.get('name', target.name)
                    target.country = target_data.get('country', target.country)
                    target.notes = target_data.get('notes', target.notes)
                    target.is_complete = target_data.get('is_complete', target.is_complete)
                    target.save()
                else:
                    # Создаем новую цель, если id не передан
                    Target.objects.create(mission=instance, **target_data)

        return instance
