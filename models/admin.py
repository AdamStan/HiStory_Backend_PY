from models.models import Answer
from django.contrib import admin
from models.models import Question, Answer, Category, AnswerType

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Category)
admin.site.register(AnswerType)