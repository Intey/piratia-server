from rest_framework.serializers import Serializer, ModelSerializer, BooleanField

from game.models import BodyAction


class BodyActionSerializer(ModelSerializer):
    class Meta:
        model = BodyAction
        fields = '__all__'


SERIALIZER_CASE = dict(
    body=BodyActionSerializer,
)
