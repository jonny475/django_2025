# Generated by Django 5.2.4 on 2025-07-31 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="update_date",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="create_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="modify_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
