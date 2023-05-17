from rest_framework import generics
import time
from rest_framework.views import APIView
from .models import User
from rest_framework.response import Response
from .serializers import UserSerializer, CountSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import math


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class UpdateCountView(APIView):
    def get(self, request):
        count = 0.01
        

        while True:
            print("old count: ", round(count, 2))
            # Your update logic here
            time.sleep(1.33)

            # Increment count
            count += 0.01
            print("new count: ", round(count, 2))

            # Create serializer instance
    # serializer = CountSerializer({'count': count})

            # Return the serialized data as the response
    # return Response(serializer.data)