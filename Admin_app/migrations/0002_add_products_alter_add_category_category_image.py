# Generated by Django 4.1.5 on 2023-02-25 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ADD_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('product_category', models.CharField(max_length=10)),
                ('product_quantity', models.IntegerField()),
                ('product_price', models.FloatField()),
                ('product_image', models.ImageField(upload_to='sample')),
            ],
        ),
        migrations.AlterField(
            model_name='add_category',
            name='category_image',
            field=models.ImageField(default='null.jpeg', upload_to='sample'),
        ),
    ]
