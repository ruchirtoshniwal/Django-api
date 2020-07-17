from django.db import models

# Create your models here.
class Tapi(models.Model):
    TYPEID = models.IntegerField(blank=False, default='',auto_created=False, primary_key=True, serialize=False, verbose_name='TYPEID')
    TYPEDISCRIPTION = models.CharField(max_length=60,blank=False, default='')

#patient api

class Papi(models.Model):
    patient_id = models.IntegerField(blank=False, default='',auto_created=False, primary_key=True, serialize=False, verbose_name='PATIENTID')
    name = models.CharField(max_length=30,blank=False, default='')
    address = models.CharField(max_length=30,blank=False, default='')
    city = models.CharField(max_length=30,blank=False, default='')
    state = models.CharField(max_length=30,blank=False, default='')
    pincode = models.CharField(max_length=30,blank=False, default='')
    phone = models.CharField(max_length=30,blank=False, default='')
    email = models.CharField(max_length=30,blank=False, default='')
    local = models.CharField(max_length=1,blank=False, default='')
    opbal = models.DecimalField(max_digits=12, decimal_places=4)
    clbal = models.DecimalField(max_digits=12, decimal_places=4)
    typeid = models.IntegerField(blank=False, default='')    


#item api

class Iapi(models.Model):
    ITEMID = models.IntegerField(blank=False, default='',auto_created=False, primary_key=True, serialize=False, verbose_name='ITEMID')
    name = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=70, blank=False, default='')
    unit = models.CharField(max_length=70, blank=False, default='')
    opstock = models.DecimalField(max_digits=12, decimal_places=4,blank=False, default='')
    clstock = models.DecimalField(max_digits=12, decimal_places=4,blank=False, default='')
    rate = models.DecimalField(max_digits=12, decimal_places=4,blank=False, default='')
    purrate = models.DecimalField(max_digits=12, decimal_places=4,blank=False, default='')
    mrp = models.DecimalField(max_digits=12, decimal_places=4,blank=False, default='')
    gstPER = models.DecimalField(max_digits=12, decimal_places=4,blank=False, default='')
    slcode = models.IntegerField(blank=False, default='')
    purcode = models.IntegerField(blank=False, default='')

#//////////////salesman api
class Smainapi(models.Model):
    INV1REFNO = models.CharField(max_length=70,blank=False, default='',auto_created=False, primary_key=True, serialize=False, verbose_name='INV1REFNO')
    INV1DATE = models.DateField()
    INV1TYPE = models.CharField(max_length=70, blank=False, default='')
    INV1PRTYCD = models.ForeignKey(Papi, to_field='patient_id', null=False,on_delete=models.CASCADE)
    NV1INVNO = models.CharField(max_length=70, blank=False, default='')
    INV1INVDT = models.DateField()
    INV1PAYTM = models.CharField(max_length=70, blank=False, default='')
    INV1DESP = models.CharField(max_length=70, blank=False, default='')
    INV1PKGS = models.CharField(max_length=70, blank=False, default='')
    INV1BROKCD = models.IntegerField(blank=False, default='')
    INV1CHLNO = models.CharField(max_length=70, blank=False, default='')
    INV1CHLDT = models.DateField()
    INV1AMT = models.DecimalField(max_digits=12, decimal_places=4)
    INV1NET = models.DecimalField(max_digits=12, decimal_places=4)
    INV1DISPER = models.DecimalField(max_digits=12, decimal_places=4)
    INV1DISAMT = models.DecimalField(max_digits=12, decimal_places=4)
    INV1GSTPER= models.DecimalField(max_digits=12, decimal_places=4)
    INV1GSTAMT = models.DecimalField(max_digits=12, decimal_places=4)
    INV1OTH = models.DecimalField(max_digits=12, decimal_places=4)
    INV1ROUND = models.DecimalField(max_digits=12, decimal_places=4)
    INV1BRAMT = models.DecimalField(max_digits=12, decimal_places=4)
    INV1DONE = models.BooleanField()
    INV1UDT = models.DateField()
    INV1EDT = models.DateField()
    INV1REMARK = models.CharField(max_length=60)    

