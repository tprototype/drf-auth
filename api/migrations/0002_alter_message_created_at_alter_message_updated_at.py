# Generated by Django 4.0.4 on 2022-05-16 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="message",
            name="updated_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
