# Generated by Django 5.1.1 on 2024-10-11 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('identity', '0010_alter_identity_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identity',
            name='id',
            field=models.CharField(default='A0k1KS3PGOlLToVmhxRVE', editable=False, max_length=21, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
