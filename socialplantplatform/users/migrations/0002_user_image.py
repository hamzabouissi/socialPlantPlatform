# Generated by Django 3.1.13 on 2021-10-30 11:17

from django.db import migrations, models
import socialplantplatform.users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=socialplantplatform.users.models.user_image_path_upload),
        ),
    ]
