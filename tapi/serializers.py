from rest_framework import serializers 
from tapi.models import Tapi,Papi,Iapi,Smainapi,Stranapi,Ledgerapi
 
 
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


class SmainapiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Smainapi
        fields = ('INV1REFNO',
        	'INV1DATE',
        	'INV1TYPE',
        	'INV1PRTYCD',
        	'NV1INVNO',
        	'INV1INVDT',
        	'INV1PAYTM',
        	'INV1DESP',
			'INV1PKGS',
			'INV1BROKCD',
			'INV1CHLNO',
			'INV1CHLDT',
			'INV1AMT',
			'INV1NET',
			'INV1DISPER',
			'INV1DISAMT',
			'INV1GSTPER',
			'INV1GSTAMT',
			'INV1OTH',
			'INV1ROUND',
			'INV1BRAMT',
			'INV1DONE',
			'INV1UDT',
			'INV1EDT',
			'INV1REMARK'
			)

class StranapiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stranapi
        fields = ('INV1REFNO',
				  'INV2DATE',
				  'INV2TYPE',
				  'INV2PRTYCD',
				  'INV2PRODCD',
				  'INV2UNIT',
				  'INV2BATCH',
				  'INV2QNT',
				  'INV2RATE',
				  'INV2AMT',
				  'INV2GSTPER',
				  'INV2GSTAMT'
				  )   


#ledger api
class LedgerapiSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Ledgerapi
        fields = ('TRNNO',
                  'TRNDATE',
                  'TRNTYPE',
                  'TRNCODE',
                  'TRNAMT',
                  'AMTTYPE',
                  'TRNNER')

class BookmasterapiSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = Bookmasterapi
        fields = ('BOOKID',
                  'BOOKNAME',
                  'BOOKTYPE',
                  'OPBAL',
                  'CLBAL',
                  'OPBAL_TYPE',
                  'CLBAL_TYPE')                                   