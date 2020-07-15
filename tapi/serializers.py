from rest_framework import serializers 
from tapi.models import Tapi
 
 
class TapiSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Tapi
        fields = ('TYPEID',
                  'TYPEDISCRIPTION')