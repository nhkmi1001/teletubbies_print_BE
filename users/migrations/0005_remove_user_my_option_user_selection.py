# Generated by Django 4.1.3 on 2022-11-27 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_initial'),
        ('users', '0004_remove_user_asd_user_my_option'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='my_option',
        ),
        migrations.AddField(
            model_name='user',
            name='selection',
            field=models.ManyToManyField(related_name='selection', to='store.filter_option'),
        ),
    ]
