# Generated by Django 5.0.6 on 2024-06-13 10:56

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[
                    ('sedan', 'sedan'),
                    ('SUV', 'SUV'),
                    ('WAGON', 'WAGON'),
                    ('coupé', 'coupé'),
                    ('racing', 'racing')
                ], max_length=30)),
                ('dealer_id', models.IntegerField()),
                ('car_make', models.ForeignKey(
                    on_delete=models.deletion.CASCADE,
                    to='djangoapp.CarMake'
                )),
            ],
        ),
    ]
