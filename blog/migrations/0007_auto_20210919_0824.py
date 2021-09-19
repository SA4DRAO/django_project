# Generated by Django 3.2.7 on 2021-09-19 04:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210919_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='isExternal',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='contents',
            field=models.TextField(default='NA', verbose_name='test'),
        ),
        migrations.AlterField(
            model_name='application',
            name='deadline',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='application',
            name='isBtech',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='isMtech',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='isPhD',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='scholarship_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='stage_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='status_accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='status_applied',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='title',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='url',
            field=models.URLField(default='NA'),
        ),
    ]
