from rest_framework import ModelSerializer

from dog.models import dog

class DogSerializer(ModelSerializer):
    class Meta:
        model = Dog
        fields = [
            'id',
            'Name',
            'slug',
            'breed',
            'age',
            'gender',
            'location',
            'content'
        ]
