
from models.models import Answer, AnswerType, Category


class SaveQuestionsFromFile:

    def __init__(self, questions):
        self.questions = questions

    def save_questions(self):
        for question in self.questions:

            type_from_db = AnswerType.objects.filter(type = question.correct_answer.type.type)
            if len(type_from_db) > 0:
                question.correct_answer.type = type_from_db[0]
            else:
                question.correct_answer.type.save()

            category_from_db = Category.objects.filter(category = question.correct_answer.category.category)
            if len(category_from_db) > 0:
                question.correct_answer.category = category_from_db[0]
            else:
                question.correct_answer.category.save()
            
            answer_from_db = Answer.objects.filter(answer = question.correct_answer.answer, 
                                                   type = question.correct_answer.type, 
                                                   category = question.correct_answer.category)
            if len(answer_from_db) > 0:
                question.correct_answer = answer_from_db[0]
            else:
                question.correct_answer.save()

            question.save()
