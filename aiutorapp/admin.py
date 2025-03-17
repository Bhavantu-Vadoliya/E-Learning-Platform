from django.contrib import admin
from .models import CustomUser, Course, Enrollment, Contact

class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [EnrollmentInline]
    list_display = ('name', 'creator', 'created_at', 'file', 'media_files', 'youtube_link')
    search_fields = ('name',)
    list_filter = ('creator',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_at')
    list_filter = ('student', 'course')

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'user_type')
    search_fields = ('username', 'email')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Contact, ContactAdmin)
