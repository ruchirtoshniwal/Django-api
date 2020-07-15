from django.shortcuts import render

# Create your views here.

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from tapi.models import Tapi
from tapi.serializers import TapiSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def tapis_list(request):
    # GET list of tapi, POST a new tapis, DELETE all tapi
    if request.method == 'GET':
        tapi = Tapi.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            tapi = tapi.filter(title__icontains=title)
        
        tapi_serializer = TapiSerializer(tapi, many=True)
        return JsonResponse(tapi_serializer.data, safe=False)

    elif request.method == 'POST':
        tapis_data = JSONParser().parse(request)
        tapis_serializer = TapiSerializer(data=tapis_data)
        if tapis_serializer.is_valid():
            tapis_serializer.save()
            return JsonResponse(tapis_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tapis_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Tapi.objects.all().delete()
        return JsonResponse({'message': '{} Tapis were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    
 
@api_view(['GET', 'PUT', 'DELETE'])
def tapis_detail(request, pk):
    # find tapis by pk (id)
    try: 
        tapis = Tapi.objects.get(pk=pk) 
    except Tapi.DoesNotExist: 
        return JsonResponse({'message': 'The tapis does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE tapis
    
    if request.method == 'GET': 
        tapis_serializer = TapiSerializer(tapis) 
        return JsonResponse(tapis_serializer.data) 
 
    elif request.method == 'PUT': 
        tapis_data = JSONParser().parse(request) 
        tapis_serializer = TapiSerializer(tapis, data=tapis_data) 
        if tapis_serializer.is_valid(): 
            tapis_serializer.save() 
            return JsonResponse(tapis_serializer.data) 
        return JsonResponse(tapis_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tapis.delete() 
        return JsonResponse({'message': 'Tapi was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT) 