# Generated by Django 5.0.1 on 2024-03-03 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postmodel',
            options={'ordering': ('-date_created',)},
        ),
    ]
