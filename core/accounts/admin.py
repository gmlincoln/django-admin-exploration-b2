from django.contrib import admin
from .models import Students


# Register your models here.
# admin.site.register(Students)

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'dept', 'student_id', 'image')
    search_fields = ('name', 'student_id')
    list_filter = ('dept',)
    ordering = ('id',)