# Generated by Django 3.2.6 on 2021-10-17 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_auto_20210913_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.CharField(blank=True, db_column='price', max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='menu',
            field=models.CharField(blank=True, db_column='menu', max_length=45, null=True),
        ),
    ]
