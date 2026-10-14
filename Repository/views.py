from django.shortcuts import render
from Repository.models import Questions
from Repository.serializers import QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class QuestionListCreateView(APIView):
    def get(self, request):
        qs = Questions.objects.all()
        serializer_instance = QuestionSerializer(qs, many=True)
        return Response(serializer_instance.data)
    
    def post(self, request):
        form_data = request.data #form_data dictionary ---> python native type
        serializer_instance = QuestionSerializer(data=form_data) # Create serializer instance with form data
        if serializer_instance.is_valid(): # Check if the data is valid according to the serializer's validation rules
            actual_data=serializer_instance.validated_data #
            Questions.objects.create(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class QuestionRetrieveUpdateDeleteView(APIView):
    def get(self, request, pk): # pk is the primary key of the question to retrieve
        qs = Questions.objects.get(id=pk) # Get the question object with the given primary key
        serializer_instance = QuestionSerializer(qs) # serialize the question object
        return Response(data=serializer_instance.data) # return the serialized data as a response
    
    
    def put(self, request, pk):
        form_data = request.data 
        serializer_instance = QuestionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            Questions.objects.filter(id=pk).update(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)