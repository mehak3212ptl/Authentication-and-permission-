from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .models import *
from .serializers import *


# Create your views here.

#------------------------------------- project level authencation 
# class Studentviewset(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = StudentModel.objects.all()
#     serializer_class = StudentSerializer

# ----------------------------------------object level authencation 

    # there are two types of  1=Basic level 
    #                         2=Session level 
    # --------------------------------------------------SESSSION LEVEL 
# class Studentviewset(viewsets.ModelViewSet):
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = StudentModel.objects.all()
#     serializer_class = StudentSerializer

#      ------------------------------------------------BASSIC LEVEL 
# class Studentviewset(viewsets.ModelViewSet):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     queryset = StudentModel.objects.all()
#     serializer_class = StudentSerializer

# -----------------------------------------------TOKEN AUTHENTICATION 
#  there are he three methods 
#  -----------------1= through admin panel 
# -------------------2= through cmd
# --------------------3= through views and urls 

class Studentviewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
