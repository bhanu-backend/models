from django.contrib import admin
from .models import Student
from django.contrib.sessions.models import Session
admin.site.register(Student)



@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['session_key', 'get_data', 'expire_date']

    def get_data(self, obj):
        return obj.get_decoded()

    get_data.short_description = 'Session Data'
