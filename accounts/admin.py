from django.contrib import admin
from accounts.models import Department, Year, Profile, Statistics2, LoginHistory2


class YearAdmin(admin.ModelAdmin):
    search_fields = ['year']


class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ['college', 'name', 'type']


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['name', 'user__username', 'year__year', 'department__name']


class LoginHistoryAdmin(admin.ModelAdmin):
    search_fields = ['user__username']


class StatisticsAdmin(admin.ModelAdmin):
    search_fields = ['date']


admin.site.register(Year, YearAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(LoginHistory2, LoginHistoryAdmin)
admin.site.register(Statistics2, StatisticsAdmin)
