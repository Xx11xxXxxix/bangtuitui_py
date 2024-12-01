# Generated by Django 5.1.3 on 2024-12-01 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EaseapiLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_name', models.CharField(max_length=100)),
                ('request_params', models.TextField()),
                ('response_data', models.JSONField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('status_code', models.IntegerField()),
                ('error_message', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bangtuitui_py_easeapi_log',
            },
        ),
        migrations.CreateModel(
            name='EaseapiUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField(unique=True)),
                ('nickname', models.CharField(blank=True, max_length=100, null=True)),
                ('music_u', models.TextField()),
                ('avatar_url', models.CharField(blank=True, max_length=255, null=True)),
                ('background_url', models.CharField(blank=True, max_length=255, null=True)),
                ('signature', models.TextField(blank=True, null=True)),
                ('birthday', models.BigIntegerField(blank=True, null=True)),
                ('gender', models.SmallIntegerField(blank=True, null=True)),
                ('province', models.IntegerField(blank=True, null=True)),
                ('city', models.IntegerField(blank=True, null=True)),
                ('vip_type', models.SmallIntegerField(blank=True, null=True)),
                ('account_type', models.SmallIntegerField(blank=True, null=True)),
                ('authority', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('detail_description', models.TextField(blank=True, null=True)),
                ('auth_status', models.SmallIntegerField(blank=True, null=True)),
                ('last_login_time', models.BigIntegerField(blank=True, null=True)),
                ('last_login_ip', models.CharField(blank=True, max_length=50, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'bangtuitui_py_easeapi_user',
            },
        ),
    ]
