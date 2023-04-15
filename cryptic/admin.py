from django.contrib import admin

# Register your models here.
from cryptic.models import *

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'question_text', 'pub_date', 'answer', 'img_url', 'points', 'difficulty', 'category')


admin.site.register(Question, QuestionAdmin)