# Generated by Django 3.2.9 on 2022-03-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_user_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='postal_code',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
