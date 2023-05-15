# Generated by Django 4.1.5 on 2023-01-23 04:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Platform', '0004_alter_post_text_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Radio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('cover', models.ImageField(upload_to='', verbose_name='coverImage')),
                ('owner', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='radios', to=settings.AUTH_USER_MODEL)),
                ('songs', models.ManyToManyField(blank=True, related_name='listeners', to='Platform.radio')),
            ],
        ),
    ]