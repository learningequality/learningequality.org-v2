# Generated by Django 3.1.7 on 2021-04-07 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0002_tracking'),
        ('people', '0003_personpage_pronouns'),
    ]

    operations = [
        migrations.AddField(
            model_name='personindexpage',
            name='call_to_action',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='utils.calltoactionsnippet'),
        ),
    ]
