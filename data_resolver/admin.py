from django.contrib import admin

# 人员
from .models import DeathStatics,MissingStatics
# 房屋
from .models import CivilStructure,MasonryStructure
# 生命线
from .models import CommDisaster,TrafficDisaster
# 次生灾害
from .models import CollapseRecord,LandslideRecord
# 震情
from .models import DisasterInfo,DisatserPrediction

# Register your models here.
# 人员
admin.site.register(DeathStatics)
admin.site.register(MissingStatics)
# 房屋
admin.site.register(CivilStructure)
admin.site.register(MasonryStructure)
# 生命线
admin.site.register(CommDisaster)
admin.site.register(TrafficDisaster)
# 次生灾害
admin.site.register(CollapseRecord)
admin.site.register(LandslideRecord)
# 震情
admin.site.register(DisasterInfo)
admin.site.register(DisatserPrediction)