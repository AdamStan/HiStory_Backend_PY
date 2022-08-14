import os
from datetime import datetime 
from models.models import Answer, AnswerType, Category


class SaveQuestionsFromFile:
    
    def __init__(self, loader):
        """Defines object which gets questions from file and saves them in database

        Args:
            loader (object): should have a method "load" and a field "questions" with list of questions.
            Method "load" should initialize questions' list.
        """
        self.loader = loader

    def save_questions(self):
        self.loader.load()
        question = self.loader.questions
        for question in question:
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
        category_from_db = Category.objects.filter(period = category.period, details=category.details)
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
    

class TemporaryFileManager:

    def __init__(self, path_to_folder_with_temp_files, file, temp_file_name=datetime.now().strftime("%y%m%d%H%M%S%f")):
        self.path = path_to_folder_with_temp_files
        self.file = file
        self.temp_file_name = temp_file_name

    def save_file(self):
        extension = self.file.name.split(".")[-1]
        path_to_temp_file = os.path.join(self.path, self.temp_file_name + "." + extension)
        with open(path_to_temp_file, 'wb+') as destination:
            for chunk in self.file.chunks():
                destination.write(chunk)
        return path_to_temp_file

    def remove_file(self):
        extension = self.file.name.split(".")[-1]
        os.remove(os.path.join(self.path, self.temp_file_name + "." + extension))
