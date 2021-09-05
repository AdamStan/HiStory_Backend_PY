from models.models import Answer, AnswerType, Category, Question
from django.contrib import admin


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'correct_answer_value', 'category_name']


class QuestionAdminLoadingFromFile(QuestionAdmin):
    add_form_template = "upload_admin.html"


class QuestionsFromFile(Question):
    class Meta:
        proxy = True


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer', 'category_name']

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionsFromFile, QuestionAdminLoadingFromFile)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Category)
admin.site.register(AnswerType)
