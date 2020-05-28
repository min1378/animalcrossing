# Generated by Django 3.0.3 on 2020-05-26 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('engname', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('birthday', models.CharField(max_length=10)),
                ('personality', models.CharField(max_length=20)),
                ('sort', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Fish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('month', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Fossil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Insect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('month', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('real', models.CharField(max_length=50)),
                ('original', models.CharField(max_length=50)),
                ('engname', models.CharField(max_length=50)),
                ('memo', models.CharField(max_length=20)),
            ],
        ),
    ]