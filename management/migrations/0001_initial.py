# Generated by Django 4.1.3 on 2022-12-31 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challan',
            fields=[
                ('ChallanNo', models.PositiveIntegerField(primary_key=True, serialize=False)),
            ],
        ),
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
            name='Jobworker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Role', models.CharField(choices=[('Office', 'Office'), ('Dyer', 'Dyer'), ('Finisher', 'Finisher'), ('Factory', 'Factory')], max_length=32)),
                ('WorkerName', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderNo', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('Quality', models.CharField(max_length=32, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='SerialNo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.customer')),
                ('Order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.order')),
                ('Quality', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.quality')),
            ],
            options={
                'unique_together': {('Customer', 'Order')},
            },
        ),
        migrations.CreateModel(
            name='OtherConsumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.PositiveIntegerField()),
                ('Colour', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.colour')),
                ('Quality', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.quality')),
            ],
        ),
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderedQuantity', models.PositiveIntegerField()),
                ('BalanceQuantity', models.PositiveIntegerField()),
                ('Colour', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.colour')),
                ('SerialNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.serialno')),
            ],
        ),
        migrations.CreateModel(
            name='OfficeStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.PositiveIntegerField()),
                ('Colour', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.colour')),
                ('Office', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.jobworker')),
                ('Quality', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.quality')),
            ],
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.PositiveBigIntegerField()),
                ('Challan', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.challan')),
                ('Colour', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.colour')),
            ],
        ),
        migrations.CreateModel(
            name='FinishingStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.PositiveIntegerField()),
                ('Colour', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.colour')),
                ('Finisher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.jobworker')),
                ('Quality', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.quality')),
            ],
        ),
        migrations.CreateModel(
            name='FactoryStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.PositiveIntegerField()),
                ('Colour', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.colour')),
                ('Factory', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.jobworker')),
                ('Quality', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.quality')),
            ],
        ),
        migrations.CreateModel(
            name='DyeingStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.PositiveIntegerField()),
                ('Colour', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.colour')),
                ('Dyer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.jobworker')),
                ('Quality', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.quality')),
            ],
        ),
        migrations.AddField(
            model_name='challan',
            name='FromName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='from_name', to='management.jobworker'),
        ),
        migrations.AddField(
            model_name='challan',
            name='Quality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.quality'),
        ),
        migrations.AddField(
            model_name='challan',
            name='ToName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='to_name', to='management.jobworker'),
        ),
    ]
