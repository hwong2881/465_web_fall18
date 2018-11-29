# Generated by Django 2.1.3 on 2018-11-26 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what_category', models.CharField(choices=[('FOOD', 'food'), ('CLOTHES', 'clothes'), ('PLANT', 'plant'), ('DRINK', 'drink'), ('ELECTRONIC', 'electronic'), ('DECORATION', 'decoration'), ('UNKNOWN', 'unknown'), ('LEISURE', 'leisure'), ('GAME', 'game'), ('OTHERS', 'others')], default='UNKNOWN', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=110)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='home_page/static/media/products_image')),
                ('stock', models.IntegerField(default=True)),
                ('available', models.BooleanField(default=True)),
                ('pdated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category_model')),
            ],
        ),
    ]
