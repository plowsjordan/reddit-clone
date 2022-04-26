# Generated by Django 4.0.4 on 2022-04-26 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_votes_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='votes_total',
        ),
        migrations.AddField(
            model_name='vote',
            name='vote_total',
            field=models.IntegerField(default=0),
        ),
    ]
