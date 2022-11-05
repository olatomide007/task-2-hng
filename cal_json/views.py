from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from . models import *
from enum import Enum


def add(a,b):
    print(a, b, "sum1")
    a = int(a)
    b = int(b)
    print(a, b, "sum")
    return a+b

def subtract(a,b):
    return a-b 

def multiply(a,b):
    return a*b

class Operator(str, Enum):
    Addition = "addition"
    Subtraction = "subtraction"
    Multiplication = "multiplication"

class CreateOperationApiView(APIView):
    def get(self, request):

         return Response({"message": "Kindly use post method to perform basic maths operation"})

    def post (self, request):
        

        x = request.data.get('x')
        y=request.data.get('y')
        
    
        operation_type=request.data.get('operation_type')
        
      
        # if  ((len(x) < 1) or (len(y) < 1) or (len(operation_type) < 1)):
        #      retur  print()n Response({"message": "Invalid Input "}, status=status.HTTP_400_BAD_REQUEST)
    
        show_operation_type = ""
        # if (not(x.isnumeric())) or (not(y.isnumeric())):
        #     return Response({"message": "Input must be integer "}, status=status.HTTP_400_BAD_REQUEST)# To display error for user

        word_bank = ["addition", "add", "minus", "subtract", "multiply", "multiplication", "subtraction"]
        
        for b in range(len(word_bank)):
            if word_bank[b] not in operation_type.lower() and b >= len(word_bank):
                return Response({"message": "Invalid Operation type"}, status=status.HTTP_400_BAD_REQUEST)



        #  For Addition

        addition_word_bank = ["add", "addition", "plus"]
        
        for addition_word in addition_word_bank:
            if addition_word in operation_type.lower():
                print(x, y, "add")
                result = add(x,y)
                show_operation_type = Operator.Addition
                return Response({"slackUsername": "Olatomide", "operation_type": show_operation_type, "result" : result })
        #  For Subtraction
        subtraction_word_bank = ["minus", "subtract", "subtraction"]
        for subtraction_word in subtraction_word_bank:
            if subtraction_word in operation_type.lower():
                result = int(x) - int(y)
                show_operation_type = Operator.Subtraction
                return Response({"slackUsername": "Olatomide", "operation_type": show_operation_type, "result" : result })
        # For Multiplication
        multiplication_word_bank = ["multiply", "times", "multiplication"]
        for multiplication_word in multiplication_word_bank:
            if multiplication_word in operation_type.lower():
                result = int(x) * int(y)
                show_operation_type = Operator.Multiplication
                return Response({"slackUsername": "Olatomide", "operation_type": show_operation_type, "result" : result })

        

        
        # print(x, y, operation_type, result )
        