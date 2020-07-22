# Generated by Django 2.1.7 on 2020-07-22 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapi', '0008_ledgerapi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmasterapi',
            fields=[
                ('BOOKID', models.IntegerField(default='', primary_key=True, serialize=False, verbose_name='BOOKID')),
                ('BOOKNAME', models.CharField(default='', max_length=70)),
                ('BOOKTYPE', models.CharField(default='', max_length=70)),
                ('OPBAL', models.DecimalField(decimal_places=4, max_digits=12)),
                ('CLBAL', models.DecimalField(decimal_places=4, max_digits=12)),
                ('OPBAL_TYPE', models.CharField(default='', max_length=70)),
                ('CLBAL_TYPE', models.CharField(default='', max_length=70)),
            ],
        ),
    ]
