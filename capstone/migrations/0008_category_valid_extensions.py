# Generated by Django 3.2.6 on 2021-09-28 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0007_item_file_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='valid_extensions',
            field=models.CharField(default=False, max_length=250),
        ),
    ]
