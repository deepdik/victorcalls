# Generated by Django 2.1.2 on 2018-11-21 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0012_auto_20181121_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='isassigned',
            field=models.NullBooleanField(),
        ),
    ]
