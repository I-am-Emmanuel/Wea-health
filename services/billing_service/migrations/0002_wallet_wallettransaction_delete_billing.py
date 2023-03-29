# Generated by Django 4.1.7 on 2023-03-29 09:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patient_service', '0002_alter_patient_options'),
        ('billing_service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(default='NGN', max_length=50)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('patient', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient_service.patient')),
            ],
        ),
        migrations.CreateModel(
            name='WalletTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('deposit', 'deposit'), ('transfer', 'transfer'), ('withdraw', 'withdraw')], max_length=200, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=100, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('status', models.CharField(default='pending', max_length=100)),
                ('paystack_payment_reference', models.CharField(blank=True, default='', max_length=100)),
                ('wallet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='billing_service.wallet')),
            ],
        ),
        migrations.DeleteModel(
            name='Billing',
        ),
    ]
