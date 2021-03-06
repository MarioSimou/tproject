# Generated by Django 2.0.5 on 2018-07-26 22:11

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20180726_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boroughs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=22, unique=True)),
                ('gss_code', models.CharField(max_length=9)),
                ('hectares', models.FloatField()),
                ('nonld_area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('freq', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Boroughs',
            },
        ),
    ]
