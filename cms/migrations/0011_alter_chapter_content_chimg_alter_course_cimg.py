# Generated by Django 5.1.5 on 2025-02-01 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_chapter_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter_content',
            name='chimg',
            field=models.ImageField(blank=True, upload_to='chaptersimg/'),
        ),
        migrations.AlterField(
            model_name='course',
            name='cimg',
            field=models.FileField(default=False, upload_to='coursevideos/'),
        ),
    ]
