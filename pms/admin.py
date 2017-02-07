# -*- coding: utf-8 -*-
from django.contrib.admin import site
from pms.models import Department, Employee, RewardPunishLevel, \
    RewardPunish, Train, TrainEmployee, Salary


site.register(Department)
site.register(Employee)
site.register(RewardPunishLevel)
site.register(RewardPunish)
site.register(Train)
site.register(TrainEmployee)
site.register(Salary)
