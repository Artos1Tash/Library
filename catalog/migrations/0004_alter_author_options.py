# Generated by Django 4.1.3 on 2023-03-25 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_language'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name']},
        ),
    ]
