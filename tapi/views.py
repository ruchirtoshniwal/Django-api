from django.shortcuts import render

# Create your views here.

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from tapi.models import Tapi,Papi,Iapi
from tapi.serializers import TapiSerializer,PapiSerializer,IapiSerializer
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

# ////////////////////// patient api        


@api_view(['GET', 'POST', 'DELETE'])
def papis_list(request):
    # GET list of patient, POST a new patients, DELETE all patient
    if request.method == 'GET':
        papi = Papi.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            papi = papi.filter(title__icontains=title)
        
        papi_serializer = PapiSerializer(papi, many=True)
        return JsonResponse(papi_serializer.data, safe=False)

    elif request.method == 'POST':
        papis_data = JSONParser().parse(request)
        papis_serializer = PapiSerializer(data=papis_data)
        if papis_serializer.is_valid():
            papis_serializer.save()
            return JsonResponse(papis_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(papis_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Papi.objects.all().delete()
        return JsonResponse({'message': '{} Patients were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    
 
@api_view(['GET', 'PUT', 'DELETE'])
def papis_detail(request, pk):
    # find patients by pk (id)
    try: 
        papis = Papi.objects.get(pk=pk) 
    except Papi.DoesNotExist: 
        return JsonResponse({'message': 'The papis does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE patients
    
    if request.method == 'GET': 
        papis_serializer = PapiSerializer(papis) 
        return JsonResponse(papis_serializer.data) 
 
    elif request.method == 'PUT': 
        papis_data = JSONParser().parse(request) 
        papis_serializer = PapiSerializer(papis, data=papis_data) 
        if papis_serializer.is_valid(): 
            papis_serializer.save() 
            return JsonResponse(papis_serializer.data) 
        return JsonResponse(papis_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        papis.delete() 
        return JsonResponse({'message': 'Patient was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)        

# ////////////////////item api

@api_view(['GET', 'POST', 'DELETE'])
def iapis_list(request):
    # GET list of item, POST a new items, DELETE all item
    if request.method == 'GET':
        iapi = Iapi.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            iapi = iapi.filter(title__icontains=title)
        
        item_serializer = IapiSerializer(iapi, many=True)
        return JsonResponse(item_serializer.data, safe=False)

    elif request.method == 'POST':
        iapis_data = JSONParser().parse(request)
        iapis_serializer = IapiSerializer(data=iapis_data)
        if iapis_serializer.is_valid():
            iapis_serializer.save()
            return JsonResponse(iapis_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(iapis_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Iapi.objects.all().delete()
        return JsonResponse({'message': '{} Items were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    
 
@api_view(['GET', 'PUT', 'DELETE'])
def iapis_detail(request, pk):
    # find items by pk (id)
    try: 
        iapis = Iapi.objects.get(pk=pk) 
    except Iapi.DoesNotExist: 
        return JsonResponse({'message': 'The items does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE items
    
    if request.method == 'GET': 
        iapis_serializer = IapiSerializer(iapis) 
        return JsonResponse(iapis_serializer.data) 
 
    elif request.method == 'PUT': 
        iapis_data = JSONParser().parse(request) 
        iapis_serializer = IapiSerializer(iapis, data=iapis_data) 
        if iapis_serializer.is_valid(): 
            iapis_serializer.save() 
            return JsonResponse(iapis_serializer.data) 
        return JsonResponse(iapis_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        iapis.delete() 
        return JsonResponse({'message': 'Item was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)        
