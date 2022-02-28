from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializer import PersonSerializer, MainSliderSerializer
from rest_framework import viewsets
from product.models import Persons,MainSlider
from django.http import HttpResponse



@api_view(['GET'])
@permission_classes([AllowAny])
def test(request):
    if request.method == 'GET':
        print(request.query_params)
        #get_value =request.query_params['id']
        message = {'name':'mohamed' , 'id':'4'}
        return Response(message)

class PersonView(viewsets.ModelViewSet):
    serializer_class = PersonSerializer

    def get_queryset(self):
        person_data = Persons.objects.all()
        return person_data

@api_view(['GET'])
@permission_classes([AllowAny])      
def getdata(request):
    person_data = Persons.objects.all()
    person_serialized = PersonSerializer(person_data , many = True)
    return Response(person_serialized.data)

def home_page(request):
    return HttpResponse("Souq El manzala")


@api_view(['GET'])
@permission_classes([AllowAny])      
def MainSiderGet(request):
    mainSlider_data = MainSlider.objects.all()
    mainSlider_data_serialized = MainSliderSerializer(mainSlider_data , many = True)
    return Response(mainSlider_data_serialized.data)