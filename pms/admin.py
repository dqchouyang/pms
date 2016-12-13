# -*- coding: utf-8 -*-
from django.contrib.admin import site
from pms.models import Department, Employee


site.register(Department)
site.register(Employee)
