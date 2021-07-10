from django.db import models

# Create your models here.
class AnswerType(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return "[AnswerType: " + self.type + "]"


class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return "[Category: " + self.category + "]"


class Answer(models.Model):
    answer = models.CharField(max_length=128)
    type = models.ForeignKey(AnswerType, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def category_name(self):
        return self.category.category

    def __str__(self):
        return "[Answer: " + self.answer + "]"


class Question(models.Model):
    text = models.TextField(max_length=256)
    correct_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def correct_answer_value(self):
        return self.correct_answer.answer

    def category_name(self):
        return self.correct_answer.category.category
