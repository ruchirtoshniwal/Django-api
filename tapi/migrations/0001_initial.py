# Generated by Django 2.1.7 on 2020-07-13 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tapi',
            fields=[
                ('TYPEID', models.IntegerField(default='', primary_key=True, serialize=False, verbose_name='TYPEID')),
                ('TYPEDISCRIPTION', models.CharField(default='', max_length=60)),
            ],
        ),
    ]