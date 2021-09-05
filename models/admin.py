from models.views import upload_file
from models.models import Answer, AnswerType, Category, Question
from django.contrib import admin


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'correct_answer_value', 'category_name']


class QuestionAdminLoadingFromFile(QuestionAdmin):
    add_form_template = "upload_admin.html"

    def _changeform_view(self, request, object_id, form_url, extra_context):
        if object_id:
            print("Question update!")
        else:
            print("FILE Upload")
            if upload_file(request):
                obj_with_meta = QuestionsFromFile()
                obj_with_meta.name_of_file = str(request.FILES['file'])
                return self.response_add(request, obj_with_meta)
        return super(QuestionAdminLoadingFromFile, self)._changeform_view(
            request, object_id, form_url, extra_context)


class QuestionsFromFile(Question):
    class Meta:
        proxy = True

    name_of_file = "DON't click!"

    def __str__(self):
        return self.name_of_file


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer', 'category_name']


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionsFromFile, QuestionAdminLoadingFromFile)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Category)
admin.site.register(AnswerType)
