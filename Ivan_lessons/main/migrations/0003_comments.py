# Generated by Django 4.1.7 on 2023-03-30 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_lesson_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(db_index=True, max_length=20)),
                ('comment', models.TextField(db_index=True, max_length=300)),
            ],
        ),
    ]