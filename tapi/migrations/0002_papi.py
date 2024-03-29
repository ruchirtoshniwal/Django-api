# Generated by Django 2.1.7 on 2020-07-16 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Papi',
            fields=[
                ('patient_id', models.IntegerField(default='', primary_key=True, serialize=False, verbose_name='PATIENTID')),
                ('name', models.CharField(default='', max_length=30)),
                ('address', models.CharField(default='', max_length=30)),
                ('city', models.CharField(default='', max_length=30)),
                ('state', models.CharField(default='', max_length=30)),
                ('pincode', models.CharField(default='', max_length=30)),
                ('phone', models.CharField(default='', max_length=30)),
                ('email', models.CharField(default='', max_length=30)),
                ('local', models.CharField(default='', max_length=1)),
                ('opbal', models.DecimalField(decimal_places=4, max_digits=12)),
                ('clbal', models.DecimalField(decimal_places=4, max_digits=12)),
                ('typeid', models.IntegerField(default='')),
            ],
        ),
    ]
