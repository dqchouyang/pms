# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from django.utils import timezone
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

    def get_leader(self):
        return Employee.objects.get(id=self.manager).name

    def get_count(self):
        return Employee.objects.filter(department=self.id).count()


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
    province = models.CharField(max_length=80, verbose_name='省')
    city = models.CharField(max_length=50, verbose_name='市')
    address = models.CharField(max_length=200, blank=True, null=True, verbose_name='详细地址')
    birth = models.DateTimeField(blank=True, null=True, verbose_name='出生日期')
    nation = models.CharField(max_length=50, verbose_name='民族')
    education = models.IntegerField(default=0, choices=EDUCATION_CHOICE, verbose_name='学历')
    height = models.FloatField(default=0.0, verbose_name='身高', help_text='CM')
    weight = models.FloatField(default=0.0, verbose_name='体重', help_text='KG')
    political = models.IntegerField(default=0, choices=POLITICAL_CHOICE, verbose_name='政治面貌')
    identity_card = models.CharField(max_length=18, verbose_name='身份证号')
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ号')
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

    def get_department(self):
        return Department.objects.get(id=self.department).name

    def get_joined(self):
        return timezone.localtime(self.joined).strftime('%Y-%m-%d %H:%M:%S')


class RewardPunishLevel(TimeStampedModel):

    level = models.CharField(max_length=50, verbose_name='奖惩等级')
    title = models.CharField(max_length=50, verbose_name='奖惩内容')

    class Meta:
        verbose_name = '奖惩等级'
        verbose_name_plural = '奖惩等级'

    def __str__(self):
        return self.title

    def all_name(self):
        return '{0}:{1}'.format(self.level, self.title)


class RewardPunish(TimeStampedModel):
    title = models.CharField(max_length=100, verbose_name='奖惩标题')
    content = models.TextField(verbose_name='奖惩内容')
    level = models.ForeignKey(RewardPunishLevel)
    user = models.ForeignKey(Employee, verbose_name='奖惩人')
    remark = models.CharField(max_length=100, verbose_name='备注', null=True, blank=True)

    class Meta:
        verbose_name = '奖惩'
        verbose_name_plural = '奖惩'

    def __str__(self):
        return self.title


class Train(TimeStampedModel):
    title = models.CharField(max_length=100, verbose_name='培训主题')
    content = models.TextField(blank=True, null=True, verbose_name='培训内容')
    start = models.DateTimeField(verbose_name='开始时间')
    end = models.DateTimeField(verbose_name='结束时间')
    trainer = models.ForeignKey(Employee, verbose_name='培训师')
    address = models.CharField(max_length=200, verbose_name='培训地点')

    class Meta:
        verbose_name = '培训'
        verbose_name_plural = '培训'

    def __str__(self):
        return self.title


class TrainEmployee(TimeStampedModel):
    train = models.ForeignKey(Train, verbose_name='培训')
    emp = models.ForeignKey(Employee, verbose_name='参与人')

    class Meta:
        verbose_name = '参与培训'
        verbose_name_plural = '参与培训'

    def __str__(self):
        return self.train.title


class Salary(TimeStampedModel):
    emp = models.ForeignKey(Employee, verbose_name='员工')
    amount = models.FloatField(default=0.0, verbose_name='总金额')
    pension = models.FloatField(default=0.0, verbose_name='养老保险')
    health = models.FloatField(default=0.0, verbose_name='医疗保险')
    work = models.FloatField(default=0.0, verbose_name='失业保险')
    birth = models.FloatField(default=0.0, verbose_name='生育保险')
    house = models.FloatField(default=0.0, verbose_name='住房公积金')
    tax = models.FloatField(default=0.0, verbose_name='扣税')
    leave = models.FloatField(default=0.0, verbose_name='迟到早退')
    no_work = models.FloatField(default=0.0, verbose_name='旷工')
    due = models.FloatField(default=0.0, verbose_name='实发工资')
    grant = models.BooleanField(default=False, verbose_name='是否发放')
    remark = models.CharField(max_length=200, verbose_name='备注')

    class Meta:
        verbose_name = '薪资'
        verbose_name_plural = '薪资'

    def __str__(self):
        return self.emp.name

    def get_created(self):
        return timezone.localtime(self.created).strftime('%Y-%m-%d')

    def get_grant(self):
        return '是' if self.grant else '否'
