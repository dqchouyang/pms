from django import forms
from pms.models import Department, Employee, RewardPunishLevel, RewardPunish


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('name', 'gender', 'tel', 'province', 'city', 'nation', 'education', 'identity_card', 'joined')

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)


class LevelForm(forms.ModelForm):

    class Meta:
        model = RewardPunishLevel
        fields = ('level', 'title')


class RewardPunishForm(forms.ModelForm):

    class Meta:
        model = RewardPunish
        fields = ('title', 'content', 'level', 'user', 'remark')
