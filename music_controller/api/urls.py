#stores all the urls local to this app
# these urls are more backwards facing meaning that the react code will be using these
from django.urls import path
from .views import RoomView, CreateRoomView,GetRoom

urlpatterns = [
    path('room',RoomView.as_view()), # if we get a url thats blank call the main function
    path('create-room', CreateRoomView.as_view()),
    path('get-room',GetRoom.as_view())
]