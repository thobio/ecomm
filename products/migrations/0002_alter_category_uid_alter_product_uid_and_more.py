# Generated by Django 4.1.7 on 2023-05-29 13:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('34e6db04-e9fc-4669-abc9-6da5eb2c431d'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('34e6db04-e9fc-4669-abc9-6da5eb2c431d'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('34e6db04-e9fc-4669-abc9-6da5eb2c431d'), editable=False, primary_key=True, serialize=False),
        ),
    ]
