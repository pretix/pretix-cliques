# Generated by Django 2.2.1 on 2019-05-07 21:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretix_cliques', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clique',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
