
from models.models import Answer, AnswerType, Category


class SaveQuestionsFromFile:

    def __init__(self, questions):
        self.questions = questions

    def save_questions(self):
        for question in self.questions:
            question.correct_answer.type = self.save_type_without_repetition(question.correct_answer.type)
            question.correct_answer.category = self.save_category_without_repetition(question.correct_answer.category)
            question.correct_answer = self.save_answer_without_repetition(question.correct_answer)

            question.save()

    def save_type_without_repetition(self, answer_type):
        type_from_db = AnswerType.objects.filter(type = answer_type.type)
        if len(type_from_db) > 0:
            return type_from_db[0]
        answer_type.save()
        return answer_type

    def save_category_without_repetition(self, category):
        category_from_db = Category.objects.filter(category = category.category)
        if len(category_from_db) > 0:
            return category_from_db[0]
        category.save()
        return category

    def save_answer_without_repetition(self, answer):
        answer_from_db = Answer.objects.filter(answer = answer.answer, 
                                               type = answer.type, 
                                               category = answer.category)
        if len(answer_from_db) > 0:
            return answer_from_db[0]
        answer.save()
        return answer
    