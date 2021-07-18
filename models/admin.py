from django.contrib.admin import options
from models.forms import QuestionForm
from models.models import Answer, AnswerType, Category, Question
from django.contrib import admin


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'correct_answer_value', 'category_name']


class QuestionAdminLoadingFromFile(QuestionAdmin):
    add_form_template = "upload_admin.html" 

    def save_form(self, request, form, change):
        print("Save form!!!")
        return super().save_form(request, form, change)

    def save_model(self, request, obj, form, change) -> None:
        print("Save model!!!")
        return super().save_model(request, obj, form, change)


class QuestionsAddingFromFile(Question):
    class Meta:
        proxy = True


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer', 'category_name']

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionsAddingFromFile, QuestionAdminLoadingFromFile)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Category)
admin.site.register(AnswerType)
