from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view

from .serializers import CalculatorSerializer, SaveSerializer, BuySerializer, GetDratSerializer
from parser.services import calculate as calculate_service
from parser.services import save as save_service
from parser.services import buy as buy_service
from parser.services import getdraft as getdraft_service


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
def save(request):
    serializer = SaveSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    success, result = save_service(**serializer.validated_data)
    return JsonResponse(result, status=200 if success else 400)


@extend_schema(
    request=BuySerializer,
    responses=BuySerializer
)
@api_view(['POST'])
def buy(request):
    serializer = BuySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    success, result = buy_service(**serializer.validated_data)
    if success:
        return JsonResponse({'total': result, 'detail': None}, status=200)
    else:
        return JsonResponse({'total': -1, 'detail': result}, status=400)


@extend_schema(
    request=GetDratSerializer,
    responses=GetDratSerializer
)
@api_view(['POST'])
def getdraft(request):
    serializer = GetDratSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    success, result = getdraft_service(**serializer.validated_data)
    if success:
        return JsonResponse({'total': result, 'detail': None}, status=200)
    else:
        return JsonResponse({'total': -1, 'detail': result}, status=400)
