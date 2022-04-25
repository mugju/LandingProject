# Generated by Django 4.0.3 on 2022-04-06 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cus_req',
            fields=[
                ('req_uid', models.AutoField(primary_key=True, serialize=False)),
                ('req_name', models.CharField(max_length=20)),
                ('req_phone', models.CharField(max_length=13)),
                ('req_med_detail', models.TextField()),
                ('req_joindate', models.DateTimeField(auto_now_add=True)),
                ('req_status', models.BooleanField(default=False)),
                ('user_uid', models.ForeignKey(db_column='user_uid', on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]