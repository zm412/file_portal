# Generated by Django 3.2.6 on 2021-09-29 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0008_category_valid_extensions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='valid_extensions',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
