from http.client import REQUEST_URI_TOO_LONG
from django.shortcuts import render
from rest_framework import generics,status
from .serializers import RoomSerializer,CreateRoomSerializer
from .models import Room
from rest_framework.views import APIView
from rest_framework.response import Response

class RoomView(generics.ListAPIView):
    # a view that is set up to return all the Room objects
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class GetRoom(APIView):
    serializer_class = RoomSerializer
    lookup_url_kwarg = 'code'

    def get(self,request, format = None):
        code = request.GET.get(self.lookup_url_kwarg) 
        # we are get the code from the URL
        #.GET we are looking for any parameters in the URL, one that is matching code
        if code != None: #makes sure we actually do have a code
            room = Room.objects.filter(code = code)
            if len(room) > 0:
                data = RoomSerializer(room[0]).data 
                # we are serializing the first room ( because there will only be one room ) and getting it's data(python dictionary)
                if self.request.session.session_key == room[0].host:
                    data['is_host'] = self.request.session.session_key
                    return Response(data,status = status.HTTP_200_OK)
            return Response({'Room Not Found': 'Invalid Room Code in Request.'},status =status.HTTP_404_NOT_FOUND)
        
        return Response({'Bad Request': 'Code Not Found.'},status = status.HTTP_404_NOT_FOUND)
class CreateRoomView(APIView):
    # APIView allows us to dispatch to the correct request
    serializer_class = CreateRoomSerializer

    def post(self,request, format = None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = self.serializer_class(data = request.data)
        # takes all our data and serializes it and gives us some python from  it
        if serializer.is_valid():
            # tells us if the two fields (guests can pause and votes to skip ) we define are valid and are in our data 
            guest_can_pause = serializer.data.get('guest_can_pause')
            votes_to_skip = serializer.data.get('votes_to_skip')
            host = self.request.session.session_key # give them same room code if a session already exists
            queryset = Room.objects.filter(host=host)

            if queryset.exists(): 
                #used for updating room
                room = queryset[0] # grabs the active room, and update its settings 
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip
                room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
                return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
            else:
                #used for creating a new room
                room = Room(host=host, guest_can_pause=guest_can_pause,
                            votes_to_skip=votes_to_skip)
                room.save()
                return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED) 
                # we pass room into roomserializer and format it as JSON send it back as status 201 for created

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)