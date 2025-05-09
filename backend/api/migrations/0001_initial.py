# Generated by Django 5.2 on 2025-05-09 04:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoplightGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Stoplight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_id', models.IntegerField()),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('direction', models.CharField(blank=True, choices=[('N', 'North'), ('NE', 'Northeast'), ('E', 'East'), ('SE', 'Southeast'), ('S', 'South'), ('SW', 'Southwest'), ('W', 'West'), ('NW', 'Northwest')], max_length=10)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stoplights', to='api.stoplightgroup')),
            ],
        ),
    ]
