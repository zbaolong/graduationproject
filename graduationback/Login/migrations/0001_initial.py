# Generated by Django 2.0.7 on 2019-05-05 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField(verbose_name='商品id')),
                ('product_price', models.CharField(blank=True, max_length=100, null=True, verbose_name='商品价格')),
                ('product_owner', models.CharField(blank=True, max_length=16, null=True, verbose_name='商品用户姓名')),
                ('product_ownerimage', models.TextField(blank=True, null=True, verbose_name='用户头像')),
                ('product_userinfo', models.CharField(blank=True, max_length=50, null=True, verbose_name='商品用户个人简介')),
                ('product_image', models.TextField(blank=True, null=True, verbose_name='商品图片')),
                ('product_name', models.CharField(max_length=200, verbose_name='商品名称')),
                ('product_house', models.CharField(blank=True, max_length=100, null=True, verbose_name='宿舍楼')),
                ('collect_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='收藏日期')),
            ],
            options={
                'verbose_name_plural': '用户收藏',
                'verbose_name': '用户收藏',
            },
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=16, null=True, verbose_name='用户姓名')),
                ('nickname', models.CharField(blank=True, max_length=16, null=True, verbose_name='用户微信名')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='出生年月')),
                ('gender', models.CharField(blank=True, choices=[('1', '男'), ('0', '女')], default='1', max_length=6, null=True, verbose_name='性别')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='年龄')),
                ('school_number', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='学号')),
                ('human_height', models.IntegerField(blank=True, null=True, verbose_name='身高')),
                ('school', models.CharField(blank=True, default='山西大学', max_length=60, null=True, verbose_name='学校')),
                ('home', models.CharField(blank=True, max_length=50, null=True, verbose_name='家乡')),
                ('profession', models.CharField(blank=True, max_length=60, null=True, verbose_name='专业')),
                ('location_house', models.CharField(blank=True, max_length=100, null=True, verbose_name='宿舍楼')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='电话')),
                ('unionId', models.CharField(blank=True, max_length=50, null=True, verbose_name='unionId')),
                ('open_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='openid')),
                ('session_key', models.CharField(blank=True, max_length=50, null=True, verbose_name='session_key')),
                ('info', models.CharField(blank=True, max_length=50, null=True, verbose_name='个人简介')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('collect_time', models.IntegerField(default=0)),
                ('image', models.CharField(blank=True, max_length=255, null=True, verbose_name='头像')),
                ('user_image', models.TextField(blank=True, null=True, verbose_name='用户上传图片')),
                ('user_interest', models.TextField(blank=True, null=True, verbose_name='用户兴趣')),
                ('user_daily', models.TextField(blank=True, null=True, verbose_name='用户日常')),
                ('is_showinfo', models.BooleanField(default=True, verbose_name='是否显示资料')),
                ('wx_location', models.CharField(blank=True, max_length=100, null=True, verbose_name='微信位置')),
            ],
            options={
                'verbose_name_plural': '用户',
                'verbose_name': '用户',
            },
        ),
        migrations.CreateModel(
            name='Usermassage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otherid', models.IntegerField(verbose_name='留言者id')),
                ('othername', models.CharField(blank=True, max_length=60, null=True, verbose_name='留言者微信名')),
                ('otherimage', models.CharField(blank=True, max_length=255, null=True, verbose_name='留言者头像')),
                ('massage_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='留言日期')),
                ('massage_info', models.TextField(blank=True, null=True, verbose_name='留言信息')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_massage', to='Login.Userinfo')),
            ],
            options={
                'verbose_name_plural': '用户留言',
                'verbose_name': '用户留言',
            },
        ),
        migrations.AddField(
            model_name='usercollection',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_collection', to='Login.Userinfo'),
        ),
    ]
