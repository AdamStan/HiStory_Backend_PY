import pandas as pd
from models.models import Answer, AnswerType, Category, Question


class LoaderXLSX:
    def __init__(self, path):
        self.questions = []
        self.path = path

    def load(self):
        sheet_index = 0
        data_frame = pd.read_excel(self.path, sheet_index)
        for index, row in data_frame.iterrows():
            category = Category(category=row['Category'])
            answer_type = AnswerType(type=row['answer_type'])
            answer = Answer(answer=row['Answer'], category=category, type=answer_type)
            question = Question(text=row['Text'], correct_answer=answer)
            self.questions.append(question)

