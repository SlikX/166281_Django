# Generated by Django 5.1.2 on 2024-10-21 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_osoba_data_dodania'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='plec',
            field=models.IntegerField(choices=[(1, 'Female'), (2, 'Male'), (3, 'Other')]),
        ),
    ]
