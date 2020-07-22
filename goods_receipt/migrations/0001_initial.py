# Generated by Django 2.0.6 on 2020-07-07 11:20

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0001_initial'),
        ('flower', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsReceipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=191)),
                ('historical_cost', models.DecimalField(decimal_places=0, max_digits=20)),
                ('receipt_quantity', models.IntegerField()),
                ('residual_quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expired_day_num', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('flower', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='goods_receipt_flower', to='flower.Flower')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.expressions.Case, related_name='goods_receipt_supplier', to='supplier.Supplier')),
            ],
            options={
                'db_table': 'goods_receipt',
            },
        ),
    ]
