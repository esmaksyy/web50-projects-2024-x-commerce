# Generated by Django 5.0.7 on 2024-10-09 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_bid_alter_listing_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.FloatField(),
        ),
        migrations.DeleteModel(
            name='Bid',
        ),
    ]
