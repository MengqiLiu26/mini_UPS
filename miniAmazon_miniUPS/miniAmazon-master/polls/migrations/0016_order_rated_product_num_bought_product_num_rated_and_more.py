# Generated by Django 4.0.4 on 2022-04-24 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_comment_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='rated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='num_bought',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='num_rated',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='total_score',
            field=models.IntegerField(default=0),
        ),
    ]
