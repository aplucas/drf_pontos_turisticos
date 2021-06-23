# Generated by Django 3.2.4 on 2021-06-23 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='latitude',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='longitude',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='linha2',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
