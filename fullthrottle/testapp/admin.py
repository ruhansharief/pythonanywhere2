from django.contrib import admin
from testapp.models import UserModel, ActivityPeroidModel

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','real_name','tz')

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user','start_time', 'end_time')

admin.site.register(UserModel,UserAdmin)
admin.site.register(ActivityPeroidModel,ActivityAdmin)
