# Generated by Django 3.2.7 on 2022-02-14 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherDetails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinatewisedata',
            name='friday',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='coordinatewisedata',
            name='friday_night',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='coordinatewisedata',
            name='gridId',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='coordinatewisedata',
            name='gridx',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='coordinatewisedata',
            name='gridy',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='coordinatewisedata',
            name='lastupdated',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='coordinatewisedata',
            name='monday',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='coordinatewisedata',
            name='monday_night',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='coordinatewisedata',
            name='saturday',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='coordinatewisedata',
            name='saturday_night',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='coordinatewisedata',
            name='sunday',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='coordinatewisedata',
            name='sunday_night',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='coordinatewisedata',
            name='thursday',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='coordinatewisedata',
            name='thursday_night',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='coordinatewisedata',
            name='today',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='coordinatewisedata',
            name='tonight',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='coordinatewisedata',
            name='tuesday',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='coordinatewisedata',
            name='tuesday_night',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='coordinatewisedata',
            name='wednesday',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='coordinatewisedata',
            name='wednesday_night',
            field=models.TextField(default=''),
        ),
    ]
