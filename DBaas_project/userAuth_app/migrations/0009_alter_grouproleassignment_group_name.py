# Generated by Django 4.2.11 on 2024-05-14 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth_app', '0008_remove_grouproleassignment_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grouproleassignment',
            name='group_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
