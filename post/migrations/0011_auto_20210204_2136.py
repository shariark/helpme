# Generated by Django 3.1.2 on 2021-02-04 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_comment_comment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_id',
            field=models.TextField(default=''),
        ),
    ]
