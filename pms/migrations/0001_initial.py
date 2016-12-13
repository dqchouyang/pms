# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-13 15:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=30, verbose_name='部门名称')),
                ('manager', models.IntegerField(blank=True, null=True, verbose_name='部门负责人')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pms.Department', verbose_name='上级部门')),
            ],
            options={
                'verbose_name': '部门',
                'verbose_name_plural': '部门',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('gender', models.IntegerField(choices=[(0, '男'), (1, '女'), (2, '保密')], default=0, verbose_name='性别')),
                ('tel', models.CharField(max_length=20, verbose_name='手机')),
                ('home_tel', models.CharField(blank=True, max_length=20, null=True, verbose_name='家庭电话')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='avatar', verbose_name='头像')),
                ('province', models.IntegerField(default=0, verbose_name='省')),
                ('city', models.IntegerField(default=0, verbose_name='市')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='详细地址')),
                ('birth', models.DateTimeField(blank=True, null=True, verbose_name='出生日期')),
                ('nation', models.IntegerField(default=0, verbose_name='民族')),
                ('education', models.IntegerField(choices=[(0, '初中'), (1, '高中'), (2, '大专'), (3, '本科'), (4, '硕士'), (5, '博士'), (6, '其他')], default=0, verbose_name='学历')),
                ('height', models.FloatField(default=0.0, help_text='CM', verbose_name='升高')),
                ('weight', models.FloatField(default=0.0, help_text='KG', verbose_name='体重')),
                ('political', models.IntegerField(choices=[(0, '群众'), (1, '团员'), (2, '党员/预备党员'), (3, '民主党派')], default=0, verbose_name='政治面貌')),
                ('identity_card', models.CharField(max_length=18, verbose_name='身份证号')),
                ('qq', models.IntegerField(blank=True, null=True, verbose_name='QQ号')),
                ('mail', models.EmailField(blank=True, max_length=254, null=True, verbose_name='邮箱')),
                ('wechat', models.CharField(blank=True, max_length=50, null=True, verbose_name='微信')),
                ('joined', models.DateTimeField(default=datetime.datetime(2016, 12, 13, 23, 19, 1, 230713), verbose_name='入职时间')),
                ('leave', models.DateTimeField(blank=True, null=True, verbose_name='离职时间')),
                ('department', models.IntegerField(blank=True, null=True, verbose_name='所属部门')),
                ('position', models.IntegerField(choices=[(0, '总裁'), (1, '副总裁'), (2, '总监'), (3, '副总监'), (4, '经理'), (5, '副经理'), (6, '组长'), (7, '员工'), (8, '其他')], default=0, verbose_name='职位')),
                ('status', models.BooleanField(default=True, help_text='true为在职', verbose_name='在职状态')),
                ('experience', models.CharField(blank=True, max_length=100, null=True, verbose_name='工作经验')),
                ('skill', models.CharField(blank=True, max_length=100, null=True, verbose_name='掌握技能')),
            ],
            options={
                'verbose_name': '职工',
                'verbose_name_plural': '职工',
            },
        ),
    ]