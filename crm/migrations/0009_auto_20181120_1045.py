# Generated by Django 2.1.2 on 2018-11-20 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_auto_20181120_1032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectdocument',
            old_name='file',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='projectdocument',
            old_name='description',
            new_name='name',
        ),
    ]