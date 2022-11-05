from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import *
from enum import Enum

class CreateOperationApiView(APIView):
    

    def post (self, request):
        # CreateOperation.objects.create(x=request.data["x"],
        #                                y =request.data["y"]
        #                                 )

        class Operator(str, Enum):
            Addition = "+"
            Substraction = "-"
            Multiplication = "*"
        
        return Response({"slackUsername": "Olatomide", "operator_type": Operator.Addition, "result" : 4 + 3})