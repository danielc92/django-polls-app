# Generated by Django 2.2.1 on 2019-05-10 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20190510_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(default='Other', max_length=10),
        ),
    ]