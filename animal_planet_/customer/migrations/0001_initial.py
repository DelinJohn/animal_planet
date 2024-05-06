# Generated by Django 5.0.4 on 2024-05-01 15:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=10)),
                ('delete_status', models.IntegerField(choices=[(1, 'Live'), (0, 'Delete')])),
                ('create_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('users', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='coustomer_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
