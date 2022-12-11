# Generated by Django 4.1.3 on 2022-12-11 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('Colour', models.CharField(max_length=32, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerName', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderNo', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('Quality', models.CharField(max_length=32, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderedQuantity', models.PositiveIntegerField()),
                ('BalanceQuantity', models.PositiveIntegerField()),
                ('Date', models.DateField()),
                ('Colour', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.colour')),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.customer')),
                ('Order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.order')),
                ('Quality', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.quality')),
            ],
        ),
    ]
