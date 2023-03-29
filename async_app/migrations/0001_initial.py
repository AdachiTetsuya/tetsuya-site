# Generated by Django 4.1.7 on 2023-03-29 12:22

from django.db import migrations, models

import async_app.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="VideoFile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "video",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=async_app.models.VideoFile.video_upload_path,
                        verbose_name="素材動画",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]