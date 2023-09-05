# Generated by Django 4.2.3 on 2023-08-31 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home_page', '0002_alter_hotel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratting', models.IntegerField()),
                ('comment', models.TextField()),
                ('Hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_page.hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]