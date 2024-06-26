# Generated by Django 5.0.4 on 2024-05-01 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.IntegerField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Dispatch', 'Dispatch'), ('On the way', 'On the way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel'), ('Return', 'Return')], default=2),
        ),
    ]
