# Generated by Django 5.1.2 on 2024-10-29 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('uploadted_at', models.DateTimeField()),
            ],
        ),
    ]
