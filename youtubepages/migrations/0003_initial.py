# Generated by Django 4.2.7 on 2023-12-27 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("youtubepages", "0002_delete_videoform"),
    ]

    operations = [
        migrations.CreateModel(
            name="VideoForm",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("CategoryId", models.IntegerField()),
                ("Category", models.CharField(max_length=30)),
                ("ChannelName", models.CharField(max_length=80)),
                ("Title", models.CharField(max_length=200)),
                ("video", models.FileField(upload_to="")),
            ],
            options={"db_table": "YoutubeVideo",},
        ),
    ]