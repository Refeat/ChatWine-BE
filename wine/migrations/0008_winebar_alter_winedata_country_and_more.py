# Generated by Django 4.2.3 on 2023-08-03 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0007_alter_conversation_timestamp_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WineBar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='winedata',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='winedata',
            name='wine_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]