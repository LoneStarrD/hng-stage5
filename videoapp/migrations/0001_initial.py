# Generated by Django 4.2.5 on 2023-09-29 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('video_file', models.FileField(upload_to='videos/')),
            ],
        ),
        migrations.CreateModel(
            name='VideoTranscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('transcription', models.TextField()),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videoapp.video')),
            ],
        ),
    ]