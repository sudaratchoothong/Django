# Generated by Django 3.2.4 on 2021-06-04 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_lms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveSmallIntegerField()),
                ('province', models.CharField(max_length=100)),
                ('opinion', models.TextField()),
            ],
        ),
    ]
