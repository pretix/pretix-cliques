# Generated by Django 3.0.10 on 2020-11-01 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0169_checkinlist_gates'),
        ('pretix_cliques', '0002_clique_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderRaffleOverride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('mode', models.CharField(max_length=180)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='raffle_override', to='pretixbase.Order')),
            ],
        ),
    ]