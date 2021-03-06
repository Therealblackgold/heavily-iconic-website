# Generated by Django 3.1.3 on 2020-11-24 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('description_1', models.CharField(blank=True, max_length=300, null=True)),
                ('price_1', models.DecimalField(blank=True, decimal_places=2, max_digits=10000, null=True)),
                ('description_2', models.CharField(blank=True, max_length=300, null=True)),
                ('price_2', models.DecimalField(blank=True, decimal_places=2, max_digits=10000, null=True)),
                ('description_3', models.CharField(blank=True, max_length=300, null=True)),
                ('price_3', models.DecimalField(blank=True, decimal_places=2, max_digits=10000, null=True)),
                ('description_4', models.CharField(blank=True, max_length=300, null=True)),
                ('price_4', models.DecimalField(blank=True, decimal_places=2, max_digits=10000, null=True)),
                ('description_5', models.CharField(blank=True, max_length=300, null=True)),
                ('price_5', models.DecimalField(blank=True, decimal_places=2, max_digits=10000, null=True)),
            ],
        ),
    ]
