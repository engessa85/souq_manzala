# Generated by Django 3.1.2 on 2022-02-28 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20220228_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productor_name', models.CharField(max_length=100)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
