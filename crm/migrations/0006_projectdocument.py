# Generated by Django 2.1.2 on 2018-11-17 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_auto_20181114_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projectdocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('projectid', models.IntegerField()),
                ('file', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'projectdocument',
                'managed': True,
            },
        ),
    ]
