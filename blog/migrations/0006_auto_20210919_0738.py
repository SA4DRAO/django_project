# Generated by Django 3.2.7 on 2021-09-19 03:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210919_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='contents',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='application',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 19, 3, 37, 11, 131762, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='isBtech',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='isMtech',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='isPhD',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='scholarship_amount',
            field=models.DecimalField(decimal_places=2, default=1234, max_digits=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='title',
            field=models.CharField(default='soething', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='url',
            field=models.URLField(default='12345'),
            preserve_default=False,
        ),
    ]