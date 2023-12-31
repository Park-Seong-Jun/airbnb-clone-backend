# Generated by Django 4.2.3 on 2023-08-04 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('country', models.CharField(default='한국', max_length=50)),
                ('city', models.CharField(default='서울', max_length=80)),
                ('address', models.CharField(max_length=250)),
                ('kind', models.CharField(choices=[('entire_place', 'Entire Place'), ('private_room', 'Private Room'), ('shared_room', 'Shared Room')], max_length=150)),
                ('price', models.PositiveIntegerField()),
                ('toilet_num', models.PositiveIntegerField()),
                ('room_num', models.PositiveIntegerField()),
                ('pet_friendly', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('amenities', models.ManyToManyField(to='rooms.amenity')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
