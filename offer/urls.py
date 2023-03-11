from django.urls import path
from .views import calculate, save

urlpatterns = [
    path('calculator/', calculate),
    path('save/', save)
]