# these urls are forward facing meaning that these will be what the users sees

from django.urls import path
from .views import index

urlpatterns = [
    path('',index),
    path('join',index),
    path('create',index),
    path('room/<str:roomCode>',index)
]