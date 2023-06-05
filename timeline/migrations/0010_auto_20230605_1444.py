# Generated by Django 3.2.19 on 2023-06-05 05:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0009_auto_20230605_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='likes_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=200),
        ),
    ]