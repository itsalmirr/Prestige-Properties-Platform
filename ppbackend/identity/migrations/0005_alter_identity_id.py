# Generated by Django 5.1.1 on 2024-09-26 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0004_alter_identity_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identity',
            name='id',
            field=models.CharField(default='KTjg0baPc9kdnwIKr-M2a', editable=False, max_length=21, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
