# Generated by Django 3.2.6 on 2022-01-13 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
