# Generated by Django 2.2.12 on 2020-05-14 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0129_projectstatus_nullable_notified_on_timeout'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectstatus',
            name='baseline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_statuses', to='core.Build'),
        ),
    ]