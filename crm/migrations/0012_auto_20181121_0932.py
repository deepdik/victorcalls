# Generated by Django 2.1.2 on 2018-11-21 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0011_auto_20181121_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='isassigned',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]