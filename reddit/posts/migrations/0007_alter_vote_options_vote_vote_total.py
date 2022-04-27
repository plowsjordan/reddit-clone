# Generated by Django 4.0.4 on 2022-04-27 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_vote_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vote',
            options={'ordering': ['-vote_total']},
        ),
        migrations.AddField(
            model_name='vote',
            name='vote_total',
            field=models.IntegerField(default=0),
        ),
    ]
