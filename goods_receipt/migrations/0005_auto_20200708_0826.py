# Generated by Django 2.0.6 on 2020-07-08 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods_receipt', '0004_auto_20200707_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsreceipt',
            name='residual_quantity',
            field=models.IntegerField(null=True),
        ),
    ]
