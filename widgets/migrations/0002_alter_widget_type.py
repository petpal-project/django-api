# Generated by Django 4.2 on 2023-04-21 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widget',
            name='type',
            field=models.CharField(choices=[('timeline', 'timeline'), ('bio', 'bio'), ('diet', 'diet'), ('health', 'health')], max_length=32),
        ),
    ]