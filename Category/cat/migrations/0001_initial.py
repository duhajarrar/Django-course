# Generated by Django 4.1 on 2022-10-11 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cat",
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
                ("catName", models.CharField(max_length=200)),
                ("catDesc", models.CharField(max_length=200)),
            ],
        ),
    ]
