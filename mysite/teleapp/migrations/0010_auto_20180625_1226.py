# Generated by Django 2.0.6 on 2018-06-25 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teleapp', '0009_employee_evaluator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='evaluator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='teleapp.Employee'),
        ),
    ]
