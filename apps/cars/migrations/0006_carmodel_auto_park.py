# Generated by Django 5.0.6 on 2024-05-20 09:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_parks', '0001_initial'),
        ('cars', '0005_remove_carmodel_body_type_remove_carmodel_engine'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='auto_park',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='auto_parks.autoparkmodel'),
            preserve_default=False,
        ),
    ]
