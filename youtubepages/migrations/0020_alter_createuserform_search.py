# Generated by Django 4.2.7 on 2024-01-10 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("youtubepages", "0019_createuserform_search"),
    ]

    operations = [
        migrations.AlterField(
            model_name="createuserform",
            name="Search",
            field=models.TextField(null=True),
        ),
    ]