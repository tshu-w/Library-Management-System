# Generated by Django 2.0 on 2017-12-22 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_auto_20171222_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='date_borrow',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='date_return',
            field=models.DateField(editable=False),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='is_lost',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='is_returned',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='lossreporting',
            name='loss_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
