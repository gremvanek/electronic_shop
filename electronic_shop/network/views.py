from rest_framework import viewsets
from .models import NetworkElement
from .serializers import NetworkElementSerializer
from rest_framework.permissions import IsAuthenticated

class NetworkElementViewSet(viewsets.ModelViewSet):
    queryset = NetworkElement.objects.all()
    serializer_class = NetworkElementSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        country = self.request.query_params.get('country')
        if country:
            queryset = queryset.filter(country=country)
        return queryset
