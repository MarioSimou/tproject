# Generated by Django 2.0.5 on 2018-08-19 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20180729_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stations_pairs_routes',
            name='end_station_id',
            field=models.ForeignKey(db_column='end_station_id', on_delete=django.db.models.deletion.CASCADE, related_name='end_stations', to='webapp.Stations', verbose_name='End Station Id'),
        ),
        migrations.AlterField(
            model_name='stations_pairs_routes',
            name='start_station_id',
            field=models.ForeignKey(db_column='start_station_id', on_delete=django.db.models.deletion.CASCADE, related_name='start_stations', to='webapp.Stations', verbose_name='Start Station Id'),
        ),
    ]
