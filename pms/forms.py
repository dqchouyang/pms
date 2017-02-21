from django import forms
from pms.models import Department, Employee, RewardPunishLevel, RewardPunish, Salary, Train


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('name', 'gender', 'tel', 'home_tel', 'picture', 'province', 'city', 'address', 'birth', 'nation',
                  'education', 'height', 'weight', 'political', 'identity_card', 'qq', 'mail', 'wechat', 'joined',
                  'leave', 'department', 'position', 'status', 'experience', 'skill')


class LevelForm(forms.ModelForm):

    class Meta:
        model = RewardPunishLevel
        fields = ('level', 'title')


class RewardPunishForm(forms.ModelForm):

    class Meta:
        model = RewardPunish
        fields = ('title', 'content', 'level', 'user', 'remark')


class TrainForm(forms.ModelForm):

    class Meta:
        model = Train
        fields = ('title', 'content', 'start', 'end', 'trainer', 'address')


class SalaryForm(forms.ModelForm):

    class Meta:
        model = Salary
        fields = ('emp', 'amount', 'pension', 'health', 'work', 'birth', 'house', 'tax', 'leave', 'no_work',
                  'due', 'grant', 'remark')
