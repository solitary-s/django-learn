# Generated by Django 3.1.3 on 2020-12-14 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('intro', models.CharField(max_length=1000)),
                ('is_hot', models.IntegerField()),
            ],
            options={
                'db_table': 'tb_subject',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('sex', models.IntegerField()),
                ('birth', models.DateField()),
                ('intro', models.CharField(max_length=1000)),
                ('photo', models.CharField(max_length=255)),
                ('good_count', models.IntegerField()),
                ('bad_count', models.IntegerField()),
            ],
            options={
                'db_table': 'tb_teacher',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('tel', models.CharField(max_length=20, verbose_name='手机号')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('last_visit', models.DateTimeField(null=True, verbose_name='最后登录时间')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'tb_user',
            },
        ),
    ]
