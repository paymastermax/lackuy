# Generated by Django 3.0.6 on 2020-06-01 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='stock_price',
            field=models.IntegerField(max_length=6),
        ),
    ]
