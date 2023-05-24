from django.urls import path
from .views import calculate, save, buy, getdraft

urlpatterns = [
    path('calculator/', calculate),
    path('save/', save),
    path('buy/', buy),
    path('getdraft', getdraft)
]