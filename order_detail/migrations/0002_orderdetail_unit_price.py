# Generated by Django 2.0.6 on 2020-07-07 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_detail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='unit_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=20),
            preserve_default=False,
        ),
    ]
