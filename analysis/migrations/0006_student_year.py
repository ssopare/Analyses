# Generated by Django 2.2.3 on 2020-01-31 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0005_student_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='analysis.Year'),
        ),
    ]
