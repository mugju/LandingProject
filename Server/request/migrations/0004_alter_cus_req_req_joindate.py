<<<<<<< HEAD
# Generated by Django 4.0.3 on 2022-04-21 11:33
=======
# Generated by Django 4.0.3 on 2022-04-22 09:46
>>>>>>> b474feccedac5f3bcee1a95ecc78dceb6307f6ea

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0003_alter_cus_req_req_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cus_req',
            name='req_joindate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
