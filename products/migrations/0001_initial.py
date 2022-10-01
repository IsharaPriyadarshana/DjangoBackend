# Generated by Django 4.1.1 on 2022-09-29 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=500)),
                ('longDesc', models.TextField(default='This contains a detailed description of the product')),
                ('price', models.FloatField()),
            ],
        )
    ]
