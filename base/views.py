from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class BookList(APIView):
    def get(self, request):
        return Response({"msg":"Authenticated"})