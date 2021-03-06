# Generated by Django 3.1.3 on 2021-01-26 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=150, null=True, verbose_name='用户名')),
                ('lastLoginIp', models.CharField(blank=True, max_length=32, null=True, verbose_name='上次登录IP')),
                ('lastLoginTime', models.DateTimeField(auto_now=True, null=True, verbose_name='上次登录时间')),
                ('failNumber', models.IntegerField(default=0, verbose_name='失败次数')),
                ('islocking', models.IntegerField(default=0, verbose_name='是否锁定')),
            ],
            options={
                'verbose_name': '登录信息表',
                'db_table': 'login_info',
            },
        ),
    ]
