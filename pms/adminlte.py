from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from pms.forms import DepartmentForm, EmployeeForm, LevelForm, RewardPunishForm, SalaryForm, TrainForm
from pms.models import Department, Employee, RewardPunishLevel, RewardPunish, Train, Salary, TrainEmployee
from adminlte.utils import Pager, AdminLTEBaseView, AdminMenu


parent_menu = AdminMenu("部门管理", icon_classes="fa-institution", sort=9000)
employee_menu = AdminMenu("职工管理", icon_classes="fa-group", sort=8000)
level_menu = AdminMenu("奖惩等级管理", icon_classes="fa-star", sort=7000)
reward_menu = AdminMenu("奖惩管理", icon_classes="fa-gift", sort=6000)
train_menu = AdminMenu("培训管理", icon_classes="fa-graduation-cap", sort=5000)
salary_menu = AdminMenu("薪资管理", icon_classes="fa-jpy", sort=4000)


class DepartmentView(AdminLTEBaseView):

    menu = AdminMenu("部门列表", parent_menu=parent_menu, sort=9098)

    def get(self, request, *args, **kwargs):
        search = request.GET.get('search')
        query = Department.objects.order_by('-created').all()

        if search:
            query = query.filter(name__contains=search)

        pager = Pager.from_request(query, request)
        return render(request, 'pms/depart_list.html',
                      context={"pager": pager})


class DepartmentCreateView(AdminLTEBaseView):

    menu = AdminMenu("部门新增", parent_menu=parent_menu, sort=9099)

    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        departments = Department.objects.all()
        return render(request, 'pms/depart_create.html',
                      context={"employees": employees, "departments": departments})

    def post(self, request, *args, **kwargs):
        form = DepartmentForm(request.POST)
        if form.is_valid():
            manager = request.POST.get('manager')
            if manager == '0':
                manager = None
            parent = request.POST.get('parent')
            if parent == '0':
                parent = None
            else:
                parent = Department.objects.get(id=parent)
            Department.objects.create(name=form.cleaned_data['name'],
                                      manager=manager,
                                      parent=parent)
        else:
            messages.add_message(request, messages.ERROR, form.errors)
        return redirect('adminlte.department')


class DepartmentEditView(AdminLTEBaseView):

    class_model = Department
    _regex_name = '^department/(?P<department_id>\d+)/edit/'

    def get(self, request, *args, **kwargs):
        department_id = kwargs.get('department_id')
        employees = Employee.objects.all()
        departments = Department.objects.all()
        department = Department.objects.get(id=department_id)
        return render(request, 'pms/depart_edit.html',
                      context={"employees": employees, "departments": departments,
                               "department": department})

    def post(self, request, department_id, *args, **kwargs):
        instance = self.class_model.objects.get(id=department_id)
        form = DepartmentForm(request.POST)
        if form.is_valid():
            manager = request.POST.get('manager')
            if manager == '0':
                manager = None
            parent = request.POST.get('parent')
            if parent == '0':
                parent = None
            else:
                parent = Department.objects.get(id=parent)
            instance.name = form.cleaned_data['name']
            instance.manager = manager
            instance.parent = parent
            instance.save()
        else:
            messages.add_message(request, messages.ERROR, form.errors)
        return redirect('adminlte.department')


class DepartmentDeleteView(AdminLTEBaseView):

    class_model = Department
    _regex_name = '^department/(?P<department_id>\d+)/delete/'

    def post(self, request, *args, **kwargs):
        department_id = kwargs.get('department_id')
        department = self.class_model.objects.get(id=department_id)
        department.delete()
        return JsonResponse(dict(code=0, result='OK'))


class EmployeeView(AdminLTEBaseView):

    menu = AdminMenu("职工列表", parent_menu=employee_menu, sort=8098)

    def get(self, request, *args, **kwargs):
        search = request.GET.get('search')
        query = Employee.objects.order_by('-created').all()

        if search:
            query = query.filter(name__contains=search)

        pager = Pager.from_request(query, request)
        return render(request, 'pms/employee_list.html',
                      context={"pager": pager})


class EmployeeEditView(AdminLTEBaseView):

    class_model = Employee
    _regex_name = '^employee/(?P<employee_id>\d+)/edit/'

    def get(self, request, *args, **kwargs):
        employee_id = kwargs.get('employee_id')
        emp = self.class_model.objects.get(id=employee_id)
        departments = Department.objects.all()
        return render(request, 'pms/employee_edit.html',
                      context={"departments": departments, 'emp': emp})

    def post(self, request, employee_id, *args, **kwargs):
        emp = self.class_model.objects.get(id=employee_id)
        form = EmployeeForm(data=request.POST, files=request.FILES, instance=emp)
        if form.is_valid():
            form.save()
            return redirect('adminlte.employee')
        else:
            messages.add_message(request, messages.ERROR, form.errors)
            departments = Department.objects.all()
            return render(request, 'pms/employee_edit.html', context={"departments": departments, 'emp': emp})


class EmployeeCreateView(AdminLTEBaseView):

    menu = AdminMenu("职工新增", parent_menu=employee_menu, sort=8099)

    def get(self, request, *args, **kwargs):
        departments = Department.objects.all()
        return render(request, 'pms/employee_create.html',
                      context={"departments": departments})

    def post(self, request, *args, **kwargs):
        form = EmployeeForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminlte.employee')
        else:
            messages.add_message(request, messages.ERROR, form.errors)
            departments = Department.objects.all()
            return render(request, 'pms/employee_create.html', context={"departments": departments})


class RewardLevelCreateView(AdminLTEBaseView):
    menu = AdminMenu("奖惩等级新增", parent_menu=level_menu, sort=7099)

    def get(self, request, *args, **kwargs):
        return render(request, 'pms/level_create.html', context={})

    def post(self, request, *args, **kwargs):
        form = LevelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminlte.reward.level')
        else:
            messages.add_message(request, messages.ERROR, form.errors)
            return render(request, 'pms/level_create.html')


class RewardLevelView(AdminLTEBaseView):
    menu = AdminMenu("奖惩等级列表", parent_menu=level_menu, sort=7098)

    def get(self, request, *args, **kwargs):
        search = request.GET.get('search')
        query = RewardPunishLevel.objects.order_by('-created').all()

        if search:
            query = query.filter(level__contains=search)

        pager = Pager.from_request(query, request)
        return render(request, 'pms/level_list.html', context={"pager": pager})


class RewardLevelEditView(AdminLTEBaseView):

    class_model = RewardPunishLevel
    _regex_name = '^reward/level/(?P<level_id>\d+)/edit/'

    def get(self, request, *args, **kwargs):
        level_id = kwargs.get('level_id')
        level = self.class_model.objects.get(id=level_id)
        return render(request, 'pms/level_edit.html',
                      context={"level": level})

    def post(self, request, *args, **kwargs):
        level_id = kwargs.get('level_id')
        form = LevelForm(request.POST)
        if form.is_valid():
            instance = self.class_model.objects.get(id=level_id)
            instance.level = request.POST.get('level')
            instance.title = request.POST.get('title')
            instance.save()
            return redirect('adminlte.reward.level')
        else:
            messages.add_message(request, messages.ERROR, form.errors)
            return render(request, 'pms/level_edit.html')


class RewardLevelDeleteView(AdminLTEBaseView):

    class_model = RewardPunishLevel
    _regex_name = '^reward/level/(?P<level_id>\d+)/delete/'

    def post(self, request, *args, **kwargs):
        level_id = kwargs.get('level_id')
        level = self.class_model.objects.get(id=level_id)
        level.delete()
        return JsonResponse(dict(code=0, result='OK'))


class RewardPunishCreateView(AdminLTEBaseView):
    menu = AdminMenu("奖惩新增", parent_menu=reward_menu, sort=6099)

    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        levels = RewardPunishLevel.objects.all()
        return render(request, 'pms/punish_create.html',
                      context={"employees": employees, "levels": levels})

    def post(self, request, *args, **kwargs):
        form = RewardPunishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminlte.reward.punish')
        else:
            messages.add_message(request, messages.ERROR, form.errors)
            return redirect('adminlte.reward.punish.create')


class RewardPunishView(AdminLTEBaseView):
    menu = AdminMenu("奖惩列表", parent_menu=reward_menu, sort=6098)

    def get(self, request, *args, **kwargs):
        search = request.GET.get('search')
        query = RewardPunish.objects.order_by('-created').all()

        if search:
            query = query.filter(title__contains=search)

        pager = Pager.from_request(query, request)
        return render(request, 'pms/punish_list.html', context={"pager": pager})


class RewardPunishEditView(AdminLTEBaseView):

    class_model = RewardPunish
    _regex_name = '^reward/punish/(?P<punish_id>\d+)/edit/'

    def get(self, request, *args, **kwargs):
        punish_id = kwargs.get('punish_id')
        punish = self.class_model.objects.get(id=punish_id)
        employees = Employee.objects.all()
        levels = RewardPunishLevel.objects.all()
        return render(request, 'pms/punish_edit.html',
                      context={"punish": punish, "employees": employees, "levels": levels})

    def post(self, request, *args, **kwargs):
        punish_id = kwargs.get('punish_id')
        form = LevelForm(request.POST)
        if form.is_valid():
            instance = self.class_model.objects.get(id=punish_id)
            instance.title = request.POST.get('title')
            instance.content = request.POST.get('content')
            instance.level = RewardPunishLevel.objects.get(id=request.POST.get('level'))
            instance.user = Employee.objects.get(id=request.POST.get('user'))
            instance.remark = request.POST.get('remark')
            instance.save()
            return redirect('adminlte.reward.punish')
        else:
            messages.add_message(request, messages.ERROR, form.errors)
            return redirect('adminlte.reward.punish.edit')


class RewardPunishDeleteView(AdminLTEBaseView):

    class_model = RewardPunish
    _regex_name = '^reward/punish/(?P<punish_id>\d+)/delete/'

    def post(self, request, *args, **kwargs):
        punish_id = kwargs.get('punish_id')
        punish = self.class_model.objects.get(id=punish_id)
        punish.delete()
        return JsonResponse(dict(code=0, result='OK'))


class TrainCreateView(AdminLTEBaseView):
    menu = AdminMenu("培训新增", parent_menu=train_menu, sort=5099)

    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        return render(request, 'pms/train_create.html',
                      context={"employees": employees})

    def post(self, request, *args, **kwargs):
        form = TrainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminlte.train')
        else:
            messages.add_message(request, messages.ERROR, form.errors)
            return redirect('adminlte.train.create')


class TrainView(AdminLTEBaseView):
    menu = AdminMenu("培训列表", parent_menu=train_menu, sort=5098)

    def get(self, request, *args, **kwargs):
        search = request.GET.get('search')
        query = Train.objects.order_by('-created').all()

        if search:
            query = query.filter(title__contains=search)

        pager = Pager.from_request(query, request)
        return render(request, 'pms/train_list.html', context={"pager": pager})


class TrainEditView(AdminLTEBaseView):

    class_model = Train
    _regex_name = '^train/(?P<train_id>\d+)/edit/'

    def get(self, request, *args, **kwargs):
        train_id = kwargs.get('train_id')
        train = self.class_model.objects.get(id=train_id)
        train_emps = TrainEmployee.objects.filter(train_id=train_id)
        train_emps_ids = train_emps.values_list('emp_id', flat=True)
        trainers = Employee.objects.all()
        employees = Employee.objects.exclude(id__in=train_emps_ids)
        levels = RewardPunishLevel.objects.all()
        return render(request, 'pms/train_edit.html',
                      context={"train": train, "employees": employees, "levels": levels,
                               "train_emps": train_emps, "trainers": trainers})

    def post(self, request, *args, **kwargs):
        train_id = kwargs.get('train_id')
        form = TrainForm(request.POST)
        if form.is_valid():
            instance = self.class_model.objects.get(id=train_id)
            instance.title = request.POST.get('title')
            instance.content = request.POST.get('content')
            instance.start = request.POST.get('start')
            instance.end = request.POST.get('end')
            instance.trainer = Employee.objects.get(id=request.POST.get('trainer'))
            instance.address = request.POST.get('address')
            instance.save()
            return redirect('adminlte.train')
        else:
            messages.add_message(request, messages.ERROR, form.errors)
            return redirect('adminlte.train.edit')


class TrainDeleteView(AdminLTEBaseView):

    class_model = Train
    _regex_name = '^train/(?P<train_id>\d+)/delete/'

    def post(self, request, *args, **kwargs):
        train_id = kwargs.get('train_id')
        train = self.class_model.objects.get(id=train_id)
        train.delete()
        return JsonResponse(dict(code=0, result='OK'))


class TrainEmployeeBatchView(AdminLTEBaseView):

    class_model = TrainEmployee
    _regex_name = 'train/employee/(?P<train_id>\d+)/batch/'

    def post(self, request, *args, **kwargs):
        train_id = kwargs.get('train_id')
        emp_ids = request.POST.get('emp_ids')
        try:
            emp_ids = emp_ids.split(',')
            emp_ids = [emp_id for emp_id in emp_ids if emp_id]
        except:
            return JsonResponse(dict(code=10050, message='emp_ids illegal'))
        flag = request.POST.get('flag', None)
        if flag not in ['on', 'off']:
            return JsonResponse(dict(code=10051, message='flag illegal'))

        if flag == 'on':
            for employee_id in emp_ids:
                try:
                    self.class_model.objects.get_or_create(train_id=train_id, emp_id=employee_id)
                except:
                    pass
        else:
            self.class_model.objects.filter(train_id=train_id).filter(emp_id__in=emp_ids).delete()

        return JsonResponse(dict(code=0, result='OK'))


class SalaryCreateView(AdminLTEBaseView):
    menu = AdminMenu("薪资新增", parent_menu=salary_menu, sort=4099)

    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        return render(request, 'pms/salary_create.html',
                      context={"employees": employees})

    def post(self, request, *args, **kwargs):
        form = SalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminlte.salary')
        else:
            messages.add_message(request, messages.ERROR, form.errors)
            return redirect('adminlte.salary.create')


class SalaryView(AdminLTEBaseView):
    menu = AdminMenu("薪资列表", parent_menu=salary_menu, sort=4098)

    def get(self, request, *args, **kwargs):
        search = request.GET.get('search')
        query = Salary.objects.order_by('-created').all()

        if search:
            query = query.filter(emp__name__contains=search)

        pager = Pager.from_request(query, request)
        return render(request, 'pms/salary_list.html', context={"pager": pager})


class SalaryEditView(AdminLTEBaseView):

    class_model = Salary
    _regex_name = '^salary/(?P<salary_id>\d+)/edit/'

    def get(self, request, *args, **kwargs):
        salary_id = kwargs.get('salary_id')
        salary = self.class_model.objects.get(id=salary_id)
        employees = Employee.objects.all()
        levels = RewardPunishLevel.objects.all()
        return render(request, 'pms/salary_edit.html',
                      context={"salary": salary, "employees": employees, "levels": levels})

    def post(self, request, *args, **kwargs):
        salary_id = kwargs.get('salary_id')
        form = SalaryForm(request.POST)
        if form.is_valid():
            instance = self.class_model.objects.get(id=salary_id)
            instance.emp = Employee.objects.get(id=request.POST.get('emp'))
            instance.amount = request.POST.get('amount')
            instance.pension = request.POST.get('pension')
            instance.health = request.POST.get('health')
            instance.work = request.POST.get('work')
            instance.birth = request.POST.get('birth')
            instance.house = request.POST.get('house')
            instance.tax = request.POST.get('tax')
            instance.leave = request.POST.get('leave')
            instance.no_work = request.POST.get('no_work')
            instance.due = request.POST.get('due')
            instance.remark = request.POST.get('remark')
            instance.grant = True if request.POST.get('grant', None) else False
            instance.save()
            return redirect('adminlte.salary')
        else:
            messages.add_message(request, messages.ERROR, form.errors)
            return redirect('adminlte.salary.edit')


class SalaryDeleteView(AdminLTEBaseView):

    class_model = Salary
    _regex_name = '^salary/(?P<salary_id>\d+)/delete/'

    def post(self, request, *args, **kwargs):
        salary_id = kwargs.get('salary_id')
        salary = self.class_model.objects.get(id=salary_id)
        salary.delete()
        return JsonResponse(dict(code=0, result='OK'))
