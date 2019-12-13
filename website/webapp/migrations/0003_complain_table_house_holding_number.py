# Generated by Django 2.1 on 2019-12-08 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_user_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complain_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complainer_name', models.CharField(max_length=20)),
                ('complainer_email', models.EmailField(max_length=254)),
                ('complainer_phone_number', models.CharField(max_length=12)),
                ('complaint_area_name', models.TextField()),
                ('complaint_postal_code', models.CharField(max_length=20)),
                ('house_holdin_number', models.CharField(max_length=10)),
                ('complain_subject', models.CharField(max_length=30)),
                ('complain', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='House_holding_number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holder_name', models.CharField(max_length=24)),
                ('holding_number', models.CharField(max_length=15)),
            ],
        ),
    ]