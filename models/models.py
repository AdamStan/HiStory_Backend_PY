from django.db import models


# Create your models here.
class AnswerType(models.Model):
    class Meta:
        db_table = "answers_types"
    type = models.CharField(max_length=64)

    def __str__(self):
        return "[AnswerType: " + self.type + "]"

    def to_dict(self):
        return {"id": self.id, "name": self.type}


class Category(models.Model):
    class Meta:
        db_table = "categories"
    period = models.CharField(max_length=64)
    details = models.CharField(max_length=128)

    def __str__(self):
        return "[Category: " + self.period + ", " + self.details + "]"

    def to_dict(self):
        return {"id": self.id, "period": self.period, "details": self.details}

class Answer(models.Model):
    class Meta:
        db_table = "answers"
    answer = models.CharField(max_length=128)
    type = models.ForeignKey(AnswerType, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def category_name(self):
        return self.category

    def __str__(self):
        return "[Answer: " + self.answer + "]"

    def to_dict(self):
        return {"id": self.id, "answer": self.answer, "type": self.type.to_dict(), "category": self.category.to_dict()}


class Question(models.Model):
    class Meta:
        db_table = "questions"
    text = models.TextField(max_length=256)
    correct_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def correct_answer_value(self):
        return self.correct_answer.answer

    def category_name(self):
        return self.correct_answer.category
