# Generated by Django 4.0.3 on 2022-04-21 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0002_remove_bill_detail_med_uid_alter_bill_user_uid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_date',
            field=models.DateField(),
        ),
    ]
