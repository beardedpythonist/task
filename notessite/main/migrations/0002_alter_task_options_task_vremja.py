# Generated by Django 4.1.7 on 2023-03-15 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('-vremja',), 'verbose_name': 'задача', 'verbose_name_plural': 'задачи'},
        ),
        migrations.AddField(
            model_name='task',
            name='vremja',
            field=models.DateTimeField(auto_now=True, verbose_name='время публикации'),
        ),
    ]