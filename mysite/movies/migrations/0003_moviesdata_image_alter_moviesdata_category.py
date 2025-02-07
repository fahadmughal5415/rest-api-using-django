# Generated by Django 5.1.6 on 2025-02-07 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviesdata_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviesdata',
            name='image',
            field=models.ImageField(default='images/movvies/noimg.jpg', upload_to='media'),
        ),
        migrations.AlterField(
            model_name='moviesdata',
            name='category',
            field=models.CharField(default='movies', max_length=200),
        ),
    ]
