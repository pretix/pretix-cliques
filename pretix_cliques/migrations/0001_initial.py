# Generated by Django 2.2.1 on 2019-05-05 15:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pretixbase', '0118_auto_20190423_0839'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=190)),
                ('password', models.CharField(max_length=190)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliques', to='pretixbase.Event')),
            ],
            options={
                'unique_together': {('event', 'name')},
            },
        ),
        migrations.CreateModel(
            name='OrderClique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField(default=False)),
                ('clique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordercliques', to='pretix_cliques.Clique')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='orderclique', to='pretixbase.Order')),
            ],
        ),
    ]
