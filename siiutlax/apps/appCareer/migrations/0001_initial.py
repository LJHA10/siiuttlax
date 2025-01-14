
# Generated by Django 5.0.6 on 2024-07-12 18:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("appAcademy", "0001_initial"),
        ("appPeriod", "0001_initial"),


    operations = [
        migrations.CreateModel(
          

            name="Career",
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
                ("name", models.CharField(max_length=100)),
                ("short_name", models.CharField(max_length=10)),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("TSU", "Tecnica Superior Universitario"),
                            ("Ing", "Ingenieria"),
                            ("Lic", "Licenciatura"),
                            ("M", "Maestria"),
                        ],
                        max_length=3,
                    ),
                ),
                ("year_plan", models.CharField(max_length=4)),
                ("status", models.BooleanField(default=True)),
                (
                    "director",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="appAcademy.professor",
                        verbose_name="Director",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subject",
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
                ("name", models.CharField(max_length=100)),
                ("total_hours", models.IntegerField()),
                ("weekly_hours", models.IntegerField()),
                ("file", models.CharField(max_length=100)),
                (
                    "career",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="appCareer.career",
                    ),
                ),
                (
                    "semester",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="appPeriod.semester",
                    ),
                ),

            ],
        ),
    ]
