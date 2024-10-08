# Generated by Django 5.0.6 on 2024-09-09 12:42

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FoodDonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_item', models.CharField(max_length=100)),
                ('quantity', models.PositiveBigIntegerField()),
                ('type', models.CharField(max_length=255)),
                ('date_donated', models.DateTimeField(default=django.utils.timezone.now)),
                ('donor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='donations.donor')),
                ('food_bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donations.foodbank')),
            ],
        ),
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient_name', models.CharField(max_length=100)),
                ('recipient_location', models.CharField(max_length=255)),
                ('date_distributed', models.DateTimeField(default=django.utils.timezone.now)),
                ('food_donation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donations.fooddonation')),
            ],
        ),
    ]
