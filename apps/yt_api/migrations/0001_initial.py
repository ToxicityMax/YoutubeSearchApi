# Generated by Django 4.1 on 2022-09-02 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="VideoDetails",
            fields=[
                (
                    "yt_id",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("keyword", models.CharField(blank=True, max_length=255, null=True)),
                ("thumbnail", models.URLField()),
                ("title", models.CharField(blank=True, max_length=511, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("channel_id", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "channel_title",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("published_at", models.DateTimeField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddIndex(
            model_name="videodetails",
            index=models.Index(
                fields=["title", "description"], name="yt_api_vide_title_73904a_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="videodetails",
            index=models.Index(
                fields=["channel_id"], name="yt_api_vide_channel_c353aa_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="videodetails",
            index=models.Index(
                fields=["keyword"], name="yt_api_vide_keyword_3b7213_idx"
            ),
        ),
    ]