from django.core.management.base import BaseCommand
from pms.models import RewardPunishLevel


class Command(BaseCommand):

    def handle(self, *args, **options):
        # 初始化奖惩等级
        data = [
            {"level": "第一等(奖)", "title": "升职"},
            {"level": "第二等(奖)", "title": "加薪"},
            {"level": "第三等(奖)", "title": "红包"},
            {"level": "第四等(奖)", "title": "表扬"},
            {"level": "第一级(惩)", "title": "开除"},
            {"level": "第二级(惩)", "title": "降职"},
            {"level": "第三级(惩)", "title": "罚款"},
            {"level": "第四级(惩)", "title": "记过"},
            {"level": "第五级(惩)", "title": "警告"},
        ]
        for d in data:
            RewardPunishLevel.objects.create(level=d['level'], title=d['title'])
        print('初始化数据完成')
