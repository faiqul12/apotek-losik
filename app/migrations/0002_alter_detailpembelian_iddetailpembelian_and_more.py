# Generated by Django 4.1.1 on 2022-09-28 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailpembelian',
            name='iddetailpembelian',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='detailpenjualan',
            name='iddetailpenjualan',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='obat',
            name='idobat',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='obat',
            name='satuan',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='pembelian',
            name='idpembelian',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='penjualan',
            name='idpenjualan',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='idsupplier',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]