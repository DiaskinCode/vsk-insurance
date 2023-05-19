from django.urls import path
from .views import calculate, buy

urlpatterns = [
    path('calculator/', calculate),
    path('buy/', buy)
]