# Generated by Django 4.1.7 on 2023-05-30 17:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profile_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('c354c2f2-0b0f-4641-b6fa-05e9c862358c'), editable=False, primary_key=True, serialize=False),
        ),
    ]
