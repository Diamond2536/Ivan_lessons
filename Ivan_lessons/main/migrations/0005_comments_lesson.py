# Generated by Django 4.1.7 on 2023-03-30 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_comment_comments_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='lesson',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='main.lesson'),
        ),
    ]
