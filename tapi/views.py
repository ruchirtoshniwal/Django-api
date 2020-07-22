from django.shortcuts import render

# Create your views here.

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from tapi.models import Tapi,Papi,Iapi,Smainapi,Stranapi,Ledgerapi,Bookmasterapi
from tapi.serializers import TapiSerializer,PapiSerializer,IapiSerializer,SmainapiSerializer,StranapiSerializer,LedgerapiSerializer,BookmasterapiSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
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
    
    
 
@api_view(['GET', 'PUT', 'DELETE'])
def tapis_detail(request, pk):
    # find tapis by pk (id)
    try: 
        tapis = Tapi.objects.get(pk=pk) 
    except Tapi.DoesNotExist: 
        return JsonResponse({'message': 'The types does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
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
        return JsonResponse({'message': 'Type was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT) 

# ////////////////////// patient api        


@api_view(['GET', 'POST'])
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
    
    
 
@api_view(['GET', 'PUT', 'DELETE'])
def papis_detail(request, pk):
    # find patients by pk (id)
    try: 
        papis = Papi.objects.get(pk=pk) 
    except Papi.DoesNotExist: 
        return JsonResponse({'message': 'The patient does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
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


#//////////////salesmain api

@api_view(['GET', 'POST'])
def smainapis_list(request):
    # GET list of salesmain, POST a new salesmains, DELETE all salesmain
    if request.method == 'GET':
        smainapi = Smainapi.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            smainapi = smainapi.filter(title__icontains=title)
        
        salesmain_serializer = SmainapiSerializer(smainapi, many=True)
        return JsonResponse(salesmain_serializer.data, safe=False)

    elif request.method == 'POST':
        smainapis_data = JSONParser().parse(request)
        smainapis_serializer = SmainapiSerializer(data=smainapis_data)
        if smainapis_serializer.is_valid():
            smainapis_serializer.save()
            return JsonResponse(smainapis_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(smainapis_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
@api_view(['GET', 'PUT', 'DELETE'])
def smainapis_detail(request, pk):
    # find salesmains by pk (id)
    try: 
        smainapis = Smainapi.objects.get(pk=pk) 
    except Smainapi.DoesNotExist: 
        return JsonResponse({'message': 'The salesmains does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE salesmains
    
    if request.method == 'GET': 
        smainapis_serializer = SmainapiSerializer(smainapis) 
        return JsonResponse(smainapis_serializer.data) 
 
    elif request.method == 'PUT': 
        smainapis_data = JSONParser().parse(request) 
        smainapis_serializer = SmainapiSerializer(smainapis, data=smainapis_data) 
        if smainapis_serializer.is_valid(): 
            smainapis_serializer.save() 
            return JsonResponse(smainapis_serializer.data) 
        return JsonResponse(smainapis_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        smainapis.delete() 
        return JsonResponse({'message': 'Salesmain was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)        

#//////////////salestran api

@api_view(['GET', 'POST', 'DELETE'])
def stranapis_list(request):
    # GET list of salestran, POST a new salestrans, DELETE all salestran
    if request.method == 'GET':
        stranapi = Stranapi.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            stranapi = stranapi.filter(title__icontains=title)
        
        salestran_serializer = StranapiSerializer(stranapi, many=True)
        return JsonResponse(salestran_serializer.data, safe=False)

    elif request.method == 'POST':
        stranapis_data = JSONParser().parse(request)
        stranapis_serializer = StranapiSerializer(data=stranapis_data)
        if stranapis_serializer.is_valid():
            stranapis_serializer.save()
            return JsonResponse(stranapis_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(stranapis_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Stranapi.objects.all().delete()
        return JsonResponse({'message': '{} Salestrans were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    
 
@api_view(['GET', 'PUT', 'DELETE'])
def stranapis_detail(request, pk):
    # find salestrans by pk (id)
    try: 
        stranapis = Stranapi.objects.get(pk=pk) 
    except Stranapi.DoesNotExist: 
        return JsonResponse({'message': 'The salestrans does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE salestrans
    
    if request.method == 'GET': 
        stranapis_serializer = StranapiSerializer(stranapis) 
        return JsonResponse(stranapis_serializer.data) 
 
    elif request.method == 'PUT': 
        stranapis_data = JSONParser().parse(request) 
        stranapis_serializer = StranapiSerializer(stranapis, data=stranapis_data) 
        if stranapis_serializer.is_valid(): 
            stranapis_serializer.save() 
            return JsonResponse(stranapis_serializer.data) 
        return JsonResponse(stranapis_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        stranapis.delete() 
        return JsonResponse({'message': 'Salestran was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)   

#//////////////Ledger api

@api_view(['GET', 'POST'])
def ledgerapis_list(request):
    # GET list of ledger, POST a new ledgers, DELETE all ledger
    if request.method == 'GET':
        ledgerapi = Ledgerapi.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            ledgerapi = ledgerapi.filter(title__icontains=title)
        
        salestran_serializer = LedgerapiSerializer(ledgerapi, many=True)
        return JsonResponse(salestran_serializer.data, safe=False)

    elif request.method == 'POST':
        ledgerapis_data = JSONParser().parse(request)
        ledgerapis_serializer = LedgerapiSerializer(data=ledgerapis_data)
        if ledgerapis_serializer.is_valid():
            ledgerapis_serializer.save()
            return JsonResponse(ledgerapis_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(ledgerapis_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
 
@api_view(['GET', 'PUT', 'DELETE'])
def ledgerapis_detail(request, pk):
    # find ledgers by pk (id)
    try: 
        ledgerapis = Ledgerapi.objects.get(pk=pk) 
    except Ledgerapi.DoesNotExist: 
        return JsonResponse({'message': 'The ledgers does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE ledgers
    
    if request.method == 'GET': 
        ledgerapis_serializer = LedgerapiSerializer(ledgerapis) 
        return JsonResponse(ledgerapis_serializer.data) 
 
    elif request.method == 'PUT': 
        ledgerapis_data = JSONParser().parse(request) 
        ledgerapis_serializer = LedgerapiSerializer(ledgerapis, data=ledgerapis_data) 
        if ledgerapis_serializer.is_valid(): 
            ledgerapis_serializer.save() 
            return JsonResponse(ledgerapis_serializer.data) 
        return JsonResponse(ledgerapis_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        ledgerapis.delete() 
        return JsonResponse({'message': 'Ledger was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


#/////////bookmaster api

@api_view(['GET', 'POST'])
def bookmasterapis_list(request):
    # GET list of bookmaster, POST a new bookmasters, DELETE all bookmaster
    if request.method == 'GET':
        bookmasterapi = Bookmasterapi.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            bookmasterapi = bookmasterapi.filter(title__icontains=title)
        
        bookmaster_serializer = BookmasterapiSerializer(bookmasterapi, many=True)
        return JsonResponse(bookmaster_serializer.data, safe=False)

    elif request.method == 'POST':
        bookmasterapis_data = JSONParser().parse(request)
        bookmasterapis_serializer = BookmasterapiSerializer(data=bookmasterapis_data)
        if bookmasterapis_serializer.is_valid():
            bookmasterapis_serializer.save()
            return JsonResponse(bookmasterapis_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(bookmasterapis_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
 
@api_view(['GET', 'PUT', 'DELETE'])
def bookmasterapis_detail(request, pk):
    # find bookmasters by pk (id)
    try: 
        bookmasterapis = Bookmasterapi.objects.get(pk=pk) 
    except Bookmasterapi.DoesNotExist: 
        return JsonResponse({'message': 'The bookmasters does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE bookmasters
    
    if request.method == 'GET': 
        bookmasterapis_serializer = BookmasterapiSerializer(bookmasterapis) 
        return JsonResponse(bookmasterapis_serializer.data) 
 
    elif request.method == 'PUT': 
        bookmasterapis_data = JSONParser().parse(request) 
        bookmasterapis_serializer = BookmasterapiSerializer(bookmasterapis, data=bookmasterapis_data) 
        if bookmasterapis_serializer.is_valid(): 
            bookmasterapis_serializer.save() 
            return JsonResponse(bookmasterapis_serializer.data) 
        return JsonResponse(bookmasterapis_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        bookmasterapis.delete() 
        return JsonResponse({'message': 'bookmaster was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)                   