from rest_framework.viewsets import ModelViewSet
from .models import (
    Gift,
    GiftRequest,
    GiftApprove,
)
from .serializers import (
    GiftSerializer,
    GiftRequestSerializer,
    GiftApproveSerializer,
)


class GiftViewSet(ModelViewSet):
    
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer

class GiftRequestViewSet(ModelViewSet):
    
    queryset = GiftRequest.objects.all()
    serializer_class = GiftRequestSerializer

class GiftApproveViewSet(ModelViewSet):
    
    queryset = GiftApprove.objects.all()
    serializer_class = GiftApproveSerializer
