from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from pms.forms import DepartmentForm, EmployeeForm
from pms.models import Department, Employee
from adminlte.utils import Pager, AdminLTEBaseView, AdminMenu


parent_menu = AdminMenu("部门管理", icon_classes="fa fa-institution", sort=9000)
employee_menu = AdminMenu("职工管理", icon_classes="fa fa-group", sort=8000)


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


class EmployeeDetailView(AdminLTEBaseView):

    class_model = Employee
    _regex_name = '^employee/(?P<employee_id>\d+)/detail/'

    def get(self, request, *args, **kwargs):
        employee_id = kwargs.get('employee_id')
        emps = self.class_model.objects.get(id=employee_id)
        return render(request, 'pms/employee_detail.html',
                      context=dict(pager=emps))

    # def post(self, request, club_id, *args, **kwargs):
    #     club = self.class_model.objects.get(id=club_id)
    #     form = ClubForm(request.POST, instance=club)
    #     if form.is_valid():
    #         form.save()
    #         messages.add_message(request, messages.SUCCESS, '修改成功')
    #         return redirect('speedx_admin.club')
    #
    #     messages.add_message(request, messages.ERROR, '参数错误')
    #
    #     return render(request, 'speedx_admin/clubs/club_list.html')


class EmployeeCreateView(AdminLTEBaseView):

    menu = AdminMenu("职工新增", parent_menu=employee_menu, sort=8099)

    def get(self, request, *args, **kwargs):
        departments = Department.objects.all()
        return render(request, 'pms/employee_create.html',
                      context={"departments": departments})

    def post(self, request, *args, **kwargs):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            pass
        else:
            messages.add_message(request, messages.ERROR, form.errors)
        return redirect('adminlte.employee')
