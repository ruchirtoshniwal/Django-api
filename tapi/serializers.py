from rest_framework import serializers 
from tapi.models import Tapi,Papi,Iapi
 
 
class TapiSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tapi
        fields = ('TYPEID',
                  'TYPEDISCRIPTION')

class PapiSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Papi
        fields = ('patient_id',
             	  'name',
                  'address',
        	      'city',
                  'state',
                  'pincode',
                  'phone',
                  'email',
                  'local',
                  'opbal',
                  'clbal',
                  'typeid')  


class IapiSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Iapi
        fields = ('ITEMID',
                  'name',
                  'description',
                  'unit',
                  'opstock',
                  'clstock',
                  'rate',
                  'purrate',
                  'mrp',
                  'gstPER',
                  'slcode',
                  'purcode')                                  