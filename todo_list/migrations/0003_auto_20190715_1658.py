# Generated by Django 2.2.2 on 2019-07-15 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_list_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
