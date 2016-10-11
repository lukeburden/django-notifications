# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils import timezone
import notifications.models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_notification_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='unseen',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notification',
            name='timestamp',
            field=models.DateTimeField(default=timezone.now),
        ),
    ]
