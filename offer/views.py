from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view

from parser.services.buy import buy_service
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
    success, result = calculate_service(**serializer.validated_data)
    if success:
        return JsonResponse({'total': result, 'detail': None}, status=200)
    else:
        return JsonResponse({'total': -1, 'detail': result}, status=400)


@extend_schema(
    request=SaveSerializer,
    responses=SaveSerializer
)
@api_view(['POST'])
def buy(request):
    serializer = SaveSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    success, result = save_service(**serializer.validated_data)
    if success:
        return JsonResponse(
            {"data": buy_service(result)},
            status=200,
        )
    else:
        return JsonResponse({'total': -1, 'detail': result}, status=400)
