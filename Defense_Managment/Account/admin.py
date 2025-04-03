from django.contrib import admin
from .models import User, Student, Professor, Project, Team
from Defense.models import DefenseSchedule, Jury, Evaluation
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'gender', 'phone_number')
    search_fields = ('username', 'email', 'phone_number')
    list_filter = ('role', 'gender')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'supervisor', 'description')
    search_fields = ('title', 'supervisor__user__username')
    list_filter = ('supervisor',)

admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Team)
admin.site.register(DefenseSchedule)
admin.site.register(Jury)
admin.site.register(Evaluation)