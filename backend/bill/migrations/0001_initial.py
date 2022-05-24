# Generated by Django 4.0.3 on 2022-05-23 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('bill_uid', models.AutoField(primary_key=True, serialize=False)),
                ('bill_total_sell', models.PositiveIntegerField(null=True)),
                ('bill_profit', models.PositiveIntegerField(null=True)),
                ('bill_date', models.DateField(null=True)),
            ],
        ),
    ]
