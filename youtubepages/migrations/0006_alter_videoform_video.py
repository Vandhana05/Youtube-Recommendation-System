# Generated by Django 4.2.7 on 2023-12-28 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("youtubepages", "0005_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="videoform",
            name="video",
            field=models.FileField(null=True, upload_to="", verbose_name=""),
        ),
    ]
