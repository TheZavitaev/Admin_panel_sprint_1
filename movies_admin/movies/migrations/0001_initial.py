# Generated by Django 3.1 on 2021-07-12 15:54

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('full_name', models.TextField(verbose_name='полное имя')),
                ('birth_date', models.DateField(null=True, verbose_name='дата рождения')),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='дата создания')),
            ],
            options={
                'verbose_name': 'персона',
                'verbose_name_plural': 'персоны',
                'db_table': 'content.person',
            },
        ),
    ]