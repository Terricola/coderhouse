# Generated by Django 4.1.2 on 2022-11-09 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0002_post_delete_posts"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="tag",
            field=models.CharField(max_length=25),
        ),
    ]
