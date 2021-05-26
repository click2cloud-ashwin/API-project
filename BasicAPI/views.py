from rest_framework import generics
from .serializers import ApiSerializer
from .models import ApiModel


# Create your views here.


class Api_Objects(generics.ListCreateAPIView):
    queryset = ApiModel.objects.all()
    serializer_class = ApiSerializer


class Api_Objects_Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApiModel.objects.all()
    serializer_class = ApiSerializer

