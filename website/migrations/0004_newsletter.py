# Generated by Django 3.2.12 on 2022-03-22 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_rename_massage_contact_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
