# Generated by Django 2.0.7 on 2019-05-05 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercollection',
            name='product_userinfo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='商品用户个人简介'),
        ),
    ]