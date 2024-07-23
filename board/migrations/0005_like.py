# Generated by Django 3.2.21 on 2024-06-12 04:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0004_remove_question_liked_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_likes', to='board.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
