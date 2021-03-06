# Generated by Django 2.1.1 on 2018-10-10 15:47

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CompanyRegistration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property_Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Property_Name', models.CharField(help_text='Your PG Name', max_length=200)),
                ('Near_College', models.CharField(help_text='Colleges with 10 Kms', max_length=200)),
                ('Address', models.CharField(help_text='Complete Address', max_length=200)),
                ('State', models.CharField(max_length=200)),
                ('Pincode', models.IntegerField(max_length=6)),
                ('Single_Price', models.IntegerField(blank=True, max_length=8, null=True)),
                ('Double_Price', models.IntegerField(blank=True, max_length=8, null=True)),
                ('Triple_Price', models.IntegerField(blank=True, max_length=8, null=True)),
                ('Quad_Price', models.IntegerField(blank=True, max_length=8, null=True)),
                ('Latitude', models.FloatField(blank=True, null=True)),
                ('Longitude', models.FloatField(blank=True, null=True)),
                ('Review', models.CharField(choices=[('Very Good', 'Very Good'), ('Good', 'Good'), ('Normal', 'Normal'), ('Bad', 'Bad')], max_length=20)),
                ('Rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=20)),
                ('Gender', models.CharField(choices=[('Boys', 'Boys'), ('Girls', 'Girls')], max_length=255)),
                ('pg_url', models.CharField(max_length=1000)),
                ('Amenities', multiselectfield.db.fields.MultiSelectField(choices=[('TABLE/CHAIR', 'TABLE/CHAIR'), ('TOILET', 'TOILET'), ('ALMIRAH', 'ALMIRAH'), ('TV', 'TV'), ('FRIDGE', 'FRIDGE'), ('WIFI', 'WIFI'), ('BED', 'BED'), ('POWER BACKUP', 'POWER BACKUP'), ('R/O WATER', 'R/O WATER'), ('GYSERS', 'GYSERS'), ('FURNISHED', 'FURNISHED'), ('LAUNDARY', 'LAUNDARY'), ('PARKING', 'PARKING')], max_length=102)),
                ('Area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CompanyRegistration.City')),
                ('Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CompanyRegistration.Company_Registration')),
            ],
        ),
    ]
