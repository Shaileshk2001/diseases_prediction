# Generated by Django 4.1.5 on 2023-02-02 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_patient_data_patient_sym1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_data',
            name='doctor',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
