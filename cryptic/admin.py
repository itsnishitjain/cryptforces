from django.contrib import admin

# Register your models here.
from cryptic.models import *

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'question_text', 'pub_date', 'answer', 'img_url', 'points', 'difficulty', 'category')

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

class LogsAdmin(admin.ModelAdmin):
    list_display = ('user', 'time', 'question', 'attempt')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(logs, LogsAdmin)
