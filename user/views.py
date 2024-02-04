from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from.serializers import *


class UserViewSet(viewsets.ModelViewSet):

    queryset = Yuridik.objects.all()
    serializer_class = YuridikSerializer

class User2ViewSet(viewsets.ModelViewSet):

    queryset = Jismoniy_Shaxs.objects.all()
    serializer_class = Jismoniy_ShaxsSerializer


class UserDetail(APIView):
    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
            serializer = YuridikSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'xato': "bu id xato"})
    
    def patch(self, request, id):
        user = Yuridik.objects.get(id=id)
        serializer = YuridikSerializer(data = request.data, instance = user, partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id):
        user = Yuridik.objects.get(id=id)
        user.delete()
        message = {'delete': 'successfully'}
        return Response(message)