# Generated by Django 4.1.7 on 2023-02-25 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat_app", "0002_userfile_alter_user_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="userfile",
            name="name",
            field=models.CharField(default="ファイル", max_length=30, verbose_name="名前"),
            preserve_default=False,
        ),
    ]