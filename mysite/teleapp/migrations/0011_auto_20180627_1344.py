# Generated by Django 2.0.6 on 2018-06-27 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teleapp', '0010_auto_20180625_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='evaluator',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='teleapp.Employee'),
        ),
    ]
