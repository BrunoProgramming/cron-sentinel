# Generated by Django 2.2 on 2019-04-30 15:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alert',
            old_name='ua',
            new_name='channels',
        ),
        migrations.RenameField(
            model_name='alert',
            old_name='data',
            new_name='msg',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='remote_addr',
        ),
        migrations.AddField(
            model_name='service',
            name='last_check_timestamp',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='service',
            unique_together={('name', 'assigned')},
        ),
    ]