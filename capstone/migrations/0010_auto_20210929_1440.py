# Generated by Django 3.2.6 on 2021-09-29 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0009_alter_category_valid_extensions'),
    ]

    operations = [
        migrations.CreateModel(
            name='File_format',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='valid_extensions',
        ),
    ]