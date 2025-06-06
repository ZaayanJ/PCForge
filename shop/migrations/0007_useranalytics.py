# Generated by Django 5.1.6 on 2025-05-04 06:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_rename_incompatibilites_product_incompatibilities'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnalytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_count', models.PositiveIntegerField(default=0)),
                ('orders_placed', models.PositiveIntegerField(default=0)),
                ('orders_worked_on', models.PositiveIntegerField(default=0)),
                ('orders_finished', models.PositiveIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
