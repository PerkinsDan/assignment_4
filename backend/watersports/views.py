from rest_framework import viewsets
from .serializers import BoatSerializer
from .models import Boat

class BoatView(viewsets.ModelViewSet):
    serializer_class = BoatSerializer
    queryset = Boat.objects.all()