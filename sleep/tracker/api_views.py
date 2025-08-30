from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import SleepSession
from .serializers import SleepSessionSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def api_sleep_list(request):
    qs = SleepSession.objects.filter(user=request.user)
    return Response(SleepSessionSerializer(qs, many=True).data)
