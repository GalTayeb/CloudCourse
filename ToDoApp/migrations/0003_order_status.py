# Generated by Django 3.0.2 on 2020-02-01 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0002_auto_20200201_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
