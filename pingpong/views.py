from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

# Create your views here.
@api_view(["GET"])
@permission_classes([AllowAny])
def ping(request):
    return Response({"response": "pong"})