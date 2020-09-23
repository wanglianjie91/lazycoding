# Generated by Django 3.0.4 on 2020-09-22 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_auto_20200922_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(default='lazycoding', max_length=200, verbose_name='描述'),
        ),
        migrations.AddField(
            model_name='category',
            name='keywords',
            field=models.CharField(default='lazycoding', max_length=50, verbose_name='关键字'),
        ),
        migrations.AddField(
            model_name='tag',
            name='description',
            field=models.CharField(default='lazycoding', max_length=200, verbose_name='描述'),
        ),
        migrations.AddField(
            model_name='tag',
            name='keywords',
            field=models.CharField(default='lazycoding', max_length=50, verbose_name='关键字'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='front.Tag', verbose_name='标签集'),
        ),
    ]
