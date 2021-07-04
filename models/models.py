from django.db import models

# Create your models here.
class AnswerType(models.Model):
    type = models.TextField(max_length=64)


class Category(models.Model):
    category = models.TextField(max_length=64)


class Answer(models.Model):
    answer = models.TextField(max_length=128)
    type = models.ForeignKey(AnswerType, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)


class Question(models.Model):
    text = models.TextField(max_length=256)
    correct_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
