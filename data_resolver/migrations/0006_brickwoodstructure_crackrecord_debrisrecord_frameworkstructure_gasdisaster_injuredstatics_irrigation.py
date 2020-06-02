# Generated by Django 3.0.5 on 2020-06-02 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_resolver', '0005_disasterinfo_landsliderecord_masonrystructure_missingstatics_trafficdisaster'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrickwoodStructure',
            fields=[
                ('id', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=12)),
                ('location', models.CharField(max_length=100)),
                ('basically_intact_square', models.CharField(max_length=6)),
                ('damaged_square', models.CharField(max_length=6)),
                ('destroyed_square', models.CharField(max_length=6)),
                ('note', models.CharField(max_length=200)),
                ('reporting_unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CrackRecord',
            fields=[
                ('id', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=12)),
                ('type', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
                ('note', models.CharField(max_length=200)),
                ('picture', models.BinaryField(max_length=8388608)),
                ('reporting_unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DebrisRecord',
            fields=[
                ('id', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=12)),
                ('type', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
                ('note', models.CharField(max_length=200)),
                ('picture', models.BinaryField(max_length=8388608)),
                ('reporting_unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FrameworkStructure',
            fields=[
                ('id', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=12)),
                ('location', models.CharField(max_length=100)),
                ('basically_intact_square', models.CharField(max_length=6)),
                ('slight_damaged_square', models.CharField(max_length=6)),
                ('moderate_damaged_square', models.CharField(max_length=6)),
                ('serious_damaged_square', models.CharField(max_length=6)),
                ('destroyed_square', models.CharField(max_length=6)),
                ('note', models.CharField(max_length=200)),
                ('reporting_unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GasDisaster',
            fields=[
                ('id', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=12)),
                ('location', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=4)),
                ('grade', models.CharField(max_length=4)),
                ('picture', models.BinaryField(max_length=8388608)),
                ('note', models.CharField(max_length=200)),
                ('reporting_unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='InjuredStatics',
            fields=[
                ('id', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=12)),
                ('number', models.IntegerField()),
                ('reporting_unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='IrrigationDisaster',
            fields=[
                ('id', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=12)),
                ('location', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=4)),
                ('grade', models.CharField(max_length=4)),
                ('picture', models.BinaryField(max_length=8388608)),
                ('note', models.CharField(max_length=200)),
                ('reporting_unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='KarstRecord',
            fields=[
                ('id', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=12)),
                ('type', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
                ('note', models.CharField(max_length=200)),
                ('picture', models.BinaryField(max_length=8388608)),
                ('reporting_unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OilDisaster',
            fields=[
                ('id', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=12)),
                ('location', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=4)),
                ('grade', models.CharField(max_length=4)),
                ('picture', models.BinaryField(max_length=8388608)),
                ('note', models.CharField(max_length=200)),
                ('reporting_unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OtherRecord',
            fields=[
                ('id', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=12)),
                ('type', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
                ('note', models.CharField(max_length=200)),
                ('picture', models.BinaryField(max_length=8388608)),
                ('reporting_unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='OtherStructure',
            fields=[
                ('id', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=12)),
                ('location', models.CharField(max_length=100)),
                ('basically_intact_square', models.CharField(max_length=6)),
                ('slight_damaged_square', models.CharField(max_length=6)),
                ('moderate_damaged_square', models.CharField(max_length=6)),
                ('serious_damaged_square', models.CharField(max_length=6)),
                ('destroyed_square', models.CharField(max_length=6)),
                ('note', models.CharField(max_length=200)),
                ('reporting_unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PowerDisaster',
            fields=[
                ('id', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=12)),
                ('location', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=4)),
                ('grade', models.CharField(max_length=4)),
                ('picture', models.BinaryField(max_length=8388608)),
                ('note', models.CharField(max_length=200)),
                ('reporting_unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SettlementRecord',
            fields=[
                ('id', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=12)),
                ('type', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
                ('note', models.CharField(max_length=200)),
                ('picture', models.BinaryField(max_length=8388608)),
                ('reporting_unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WaterDisaster',
            fields=[
                ('id', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=12)),
                ('location', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=4)),
                ('grade', models.CharField(max_length=4)),
                ('picture', models.BinaryField(max_length=8388608)),
                ('note', models.CharField(max_length=200)),
                ('reporting_unit', models.CharField(max_length=50)),
            ],
        ),
    ]
