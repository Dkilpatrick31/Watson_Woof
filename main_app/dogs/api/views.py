from rest_framework.generics import ListAPIView


from dogs.models import Dog
from .serializers import DogSerializer

class DogListAPIView(ListAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
