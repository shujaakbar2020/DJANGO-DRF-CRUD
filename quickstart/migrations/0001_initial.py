# Generated by Django 3.2 on 2021-10-18 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('author', models.CharField(blank=True, max_length=255, null=True)),
                ('chapter', models.IntegerField()),
                ('type', models.IntegerField(choices=[(1, 'Holy'), (2, 'Action'), (3, 'Fantasy'), (4, 'Historical'), (5, 'Horror')], default=3, null=True)),
            ],
        ),
    ]
