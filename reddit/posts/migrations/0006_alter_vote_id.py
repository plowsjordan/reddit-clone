# Generated by Django 4.0.4 on 2022-04-27 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_vote_options_remove_vote_vote_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
