# Generated by Django 5.0.3 on 2024-04-18 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0019_devent_status_alter_catevent_expense'),
    ]

    operations = [
        migrations.AddField(
            model_name='devent',
            name='collected',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='devent',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
