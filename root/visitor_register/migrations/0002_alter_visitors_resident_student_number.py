# Generated by Django 3.2.6 on 2021-08-29 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitors',
            name='resident_student_number',
            field=models.CharField(max_length=6),
        ),
    ]
