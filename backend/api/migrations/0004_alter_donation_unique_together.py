# Generated by Django 5.1.1 on 2024-10-25 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_donation_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='donation',
            unique_together=set(),
        ),
    ]
