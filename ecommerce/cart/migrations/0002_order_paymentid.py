# Generated by Django 2.2.6 on 2019-10-08 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paymentId',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
