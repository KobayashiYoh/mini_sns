# Generated by Django 3.2.19 on 2023-05-26 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0004_alter_post_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default='652d6aebab854c499eee7fc05e362346', editable=False, primary_key=True, serialize=False),
        ),
    ]