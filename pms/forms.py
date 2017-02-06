from django import forms
from pms.models import Department, Employee


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
