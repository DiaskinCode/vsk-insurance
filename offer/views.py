from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view

from .serializers import CalculatorSerializer, SaveSerializer
from parser.services import calculate as calculate_service
from parser.services import save as save_service


@extend_schema(
    request=CalculatorSerializer,
    responses=CalculatorSerializer
)
@api_view(['POST'])
def calculate(request):
    serializer = CalculatorSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    try:
        result = calculate_service(**serializer.validated_data)
        return JsonResponse({'total': result}, status=200)
    except:
        return JsonResponse({'total': -1}, status=400)


@extend_schema(
    request=SaveSerializer,
    responses=SaveSerializer
)
@api_view(['POST'])
def save(request):
    serializer = SaveSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    try:
        result = save_service(**serializer.validated_data)
        return JsonResponse({'total': result}, status=200)
    except:
        return JsonResponse({'total': -1}, status=400)
