# Generated by Django 3.1.7 on 2021-08-29 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitor_register', '0003_auto_20210829_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitors',
            name='resident_student_number',
            field=models.CharField(max_length=50),
        ),
    ]