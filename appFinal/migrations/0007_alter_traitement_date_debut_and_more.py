# Generated by Django 5.0.6 on 2024-06-25 16:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appFinal', '0006_alter_patient_code_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traitement',
            name='date_debut',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='traitement',
            name='date_fin',
            field=models.DateField(default=datetime.date.today),
        ),
    ]