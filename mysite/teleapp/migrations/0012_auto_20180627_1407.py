# Generated by Django 2.0.6 on 2018-06-27 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teleapp', '0011_auto_20180627_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='evaluator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teleapp.Employee'),
        ),
    ]