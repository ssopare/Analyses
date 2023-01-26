# Generated by Django 2.2.3 on 2020-01-31 15:18

import analysis.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0006_student_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.ForeignKey(blank=True, default=analysis.models.getCurrentYear, null=True, on_delete=django.db.models.deletion.SET_NULL, to='analysis.Year'),
        ),
    ]
