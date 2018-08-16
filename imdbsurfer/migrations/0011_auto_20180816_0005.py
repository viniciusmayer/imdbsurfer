# Generated by Django 2.1 on 2018-08-16 00:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('imdbsurfer', '0010_auto_20180721_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dh_create', models.DateTimeField(auto_now_add=True)),
                ('dh_update', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('obs', models.CharField(blank=True, max_length=255, null=True)),
                ('key', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('user_create', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='imdbsurfer_configuration_create_related', to=settings.AUTH_USER_MODEL)),
                ('user_update', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='imdbsurfer_configuration_update_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['-index', '-year']},
        ),
    ]
