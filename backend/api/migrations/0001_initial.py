# Generated by Django 5.1.1 on 2024-10-22 14:35

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='IncomeEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('month', models.CharField(max_length=20)),
                ('year', models.IntegerField(default=2024)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.familymember')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_amount', models.IntegerField()),
                ('date_of_donation', models.DateField(default=datetime.date.today)),
                ('charity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.charity')),
                ('income_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.incomeentry')),
            ],
            options={
                'unique_together': {('income_entry', 'charity')},
            },
        ),
    ]
