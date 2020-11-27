# Generated by Django 3.1.2 on 2020-11-26 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0008_shoping_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='GAME_DATA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('link', models.CharField(max_length=2000)),
                ('image', models.FileField(blank=True, null=True, upload_to='upload')),
            ],
        ),
    ]
