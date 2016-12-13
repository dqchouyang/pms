# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from model_utils import Choices
from model_utils.models import TimeStampedModel


class Department(TimeStampedModel):
    name = models.CharField(max_length=30, verbose_name='部门名称')
    manager = models.IntegerField(blank=True, null=True, verbose_name='部门负责人')
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name='上级部门')

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = '部门'

    def __str__(self):
        return self.name


class Employee(TimeStampedModel):

    GENDER_CHOICE = Choices(
        (0, 'Male', '男'),
        (1, 'Female', '女'),
        (2, 'Secret', '保密'),
    )

    EDUCATION_CHOICE = Choices(
        (0, 'Junior', '初中'),
        (1, 'Senior', '高中'),
        (2, 'Specialty', '大专'),
        (3, 'College', '本科'),
        (4, 'Master', '硕士'),
        (5, 'Doctor', '博士'),
        (6, 'Other', '其他'),
    )

    POLITICAL_CHOICE = Choices(
        (0, 'Common', '群众'),
        (1, 'Member', '团员'),
        (2, 'Party', '党员/预备党员'),
        (3, 'Democratic', '民主党派'),
    )

    POSITION_CHOICE = Choices(
        (0, 'CEO', '总裁'),
        (1, 'VP', '副总裁'),
        (2, 'CO', '总监'),
        (3, 'DO', '副总监'),
        (4, 'GM', '经理'),
        (5, 'BM', '副经理'),
        (6, 'GH', '组长'),
        (7, 'EM', '员工'),
        (8, 'OT', '其他'),
    )

    name = models.CharField(max_length=50, verbose_name='姓名')
    gender = models.IntegerField(default=0, choices=GENDER_CHOICE, verbose_name='性别')
    tel = models.CharField(max_length=20, verbose_name='手机')
    home_tel = models.CharField(max_length=20, blank=True, null=True, verbose_name='家庭电话')
    picture = models.ImageField(null=True, blank=True, upload_to='avatar', verbose_name='头像')
    province = models.IntegerField(default=0, verbose_name='省')
    city = models.IntegerField(default=0, verbose_name='市')
    address = models.CharField(max_length=200, blank=True, null=True, verbose_name='详细地址')
    birth = models.DateTimeField(blank=True, null=True, verbose_name='出生日期')
    nation = models.IntegerField(default=0, verbose_name='民族')
    education = models.IntegerField(default=0, choices=EDUCATION_CHOICE, verbose_name='学历')
    height = models.FloatField(default=0.0, verbose_name='升高', help_text='CM')
    weight = models.FloatField(default=0.0, verbose_name='体重', help_text='KG')
    political = models.IntegerField(default=0, choices=POLITICAL_CHOICE, verbose_name='政治面貌')
    identity_card = models.CharField(max_length=18, verbose_name='身份证号')
    qq = models.IntegerField(blank=True, null=True, verbose_name='QQ号')
    mail = models.EmailField(blank=True, null=True, verbose_name='邮箱')
    wechat = models.CharField(max_length=50, blank=True, null=True, verbose_name='微信')
    joined = models.DateTimeField(default=datetime.now(), verbose_name='入职时间')
    leave = models.DateTimeField(blank=True, null=True, verbose_name='离职时间')
    department = models.IntegerField(blank=True, null=True, verbose_name='所属部门')
    position = models.IntegerField(default=0, choices=POSITION_CHOICE, verbose_name='职位')
    status = models.BooleanField(default=True, verbose_name='在职状态', help_text='true为在职')
    experience = models.CharField(max_length=100, blank=True, null=True, verbose_name='工作经验')
    skill = models.CharField(max_length=100, blank=True, null=True, verbose_name='掌握技能')

    class Meta:
        verbose_name = '职工'
        verbose_name_plural = '职工'

    def __str__(self):
        return self.name
