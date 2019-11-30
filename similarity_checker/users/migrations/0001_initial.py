# Generated by Django 3.0b1 on 2019-11-15 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstfile', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='File2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secondfile', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sameprograms', models.CharField(max_length=50)),
                ('percent', models.FloatField(max_length=10)),
                ('sno1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.File1')),
            ],
        ),
    ]