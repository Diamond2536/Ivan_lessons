from django.contrib import admin
from .models import Lesson, Comments



# Register your models here.
class CommentsInline(admin.TabularInline):
    model = Comments

class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    inlines = [CommentsInline]
admin.site.register(Lesson, LessonAdmin)


