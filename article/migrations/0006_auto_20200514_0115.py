# Generated by Django 3.0.5 on 2020-05-13 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20200514_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Eklenme Zamanı'),
        ),
    ]
