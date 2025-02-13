# Generated by Django 5.1.2 on 2024-10-25 16:57

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoPaymentMethod',
            fields=[
                ('uuid', models.CharField(max_length=36, primary_key=True, serialize=False, unique=True)),
                ('payment_type', models.CharField(max_length=255)),
                ('payment_details', models.CharField(max_length=255)),
                ('payment_status', models.CharField(max_length=255)),
                ('payment_validation', models.CharField(max_length=255))
            ]
        )
    ]
