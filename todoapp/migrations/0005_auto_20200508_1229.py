# Generated by Django 3.0.6 on 2020-05-08 17:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_auto_20200507_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
