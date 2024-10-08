# Generated by Django 5.0.6 on 2024-07-14 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20240625_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPolicySection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='account',
            name='agree',
            field=models.BooleanField(db_default=False),
        ),
        migrations.CreateModel(
            name='PrivacyPolicySubSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('order', models.IntegerField(default=0)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subsections', to='accounts.privacypolicysection')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
