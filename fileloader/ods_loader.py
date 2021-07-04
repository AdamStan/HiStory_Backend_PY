from models.models import Answer, AnswerType, Category, Question
from pandas_ods_reader import read_ods


class LoaderODS:
    def __init__(self, path):
        self.questions = []
        self.path = path

    def load(self):
        sheet_index = 0
        data_frame = read_ods(self.path, sheet_index)
        for index, row in data_frame.iterrows():
            category = Category(category=row['Category'])
            answer_type = AnswerType(type=row['answer_type'])
            answer = Answer(answer=row['Answer'], category=category, type=answer_type)
            question = Question(text=row['Text'], correct_answer=answer)
            self.questions.append(question)

