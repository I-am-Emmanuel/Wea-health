# Generated by Django 4.1.3 on 2023-04-26 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appointment_service', '0001_initial'),
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentmodel',
            name='medical_personel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.medicalpersonnel'),
        ),
    ]
