# Generated by Django 4.0.3 on 2022-04-29 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Med_salt',
            fields=[
                ('salt_uid', models.AutoField(primary_key=True, serialize=False)),
                ('salt_name', models.CharField(max_length=100)),
                ('salt_qty', models.DecimalField(decimal_places=3, max_digits=5)),
                ('salt_qty_type', models.CharField(max_length=20)),
                ('salt_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('med_uid', models.AutoField(primary_key=True, serialize=False)),
                ('med_name', models.CharField(max_length=100)),
                ('med_type', models.CharField(max_length=8)),
                ('med_buyprice', models.PositiveIntegerField()),
                ('med_sellprice', models.PositiveIntegerField()),
                ('med_cgst', models.PositiveSmallIntegerField()),
                ('med_sgst', models.PositiveSmallIntegerField()),
                ('med_expire', models.DateField()),
                ('med_mfg', models.DateField()),
                ('med_desc', models.TextField()),
                ('med_instock', models.PositiveIntegerField()),
                ('med_qty', models.PositiveSmallIntegerField()),
                ('med_company', models.CharField(max_length=30)),
            ],
        ),
    ]
