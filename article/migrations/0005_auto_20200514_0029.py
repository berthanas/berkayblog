# Generated by Django 3.0.5 on 2020-05-13 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_content',
            field=models.TextField(max_length=500, verbose_name='Yorum'),
        ),
    ]