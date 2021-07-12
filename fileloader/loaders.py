from abc import abstractmethod
from models.models import Answer, AnswerType, Category, Question
from pandas_ods_reader import read_ods
import pandas as pd


class Loader:
    def __init__(self, path):
        self.questions = []
        self.path = path

    @abstractmethod
    def load(self):
        sheet_index = 0
        data_frame = self.read(sheet_index)
        for index, row in data_frame.iterrows():
            category = Category(category=row['Category'])
            answer_type = AnswerType(type=row['answer_type'])
            answer = Answer(answer=row['Answer'], category=category, type=answer_type)
            question = Question(text=row['Text'], correct_answer=answer)
            self.questions.append(question)

    def read(self, sheet_index):
        raise Exception("Not implemented method!")


class LoaderODS(Loader):
    def __init__(self, path):
        super().__init__(path)
    
    def read(self, sheet_index):
        return read_ods(self.path, sheet_index)


class LoaderXLSX(Loader):
    def __init__(self, path):
        super().__init__(path)

    def read(self, sheet_index):
        return pd.read_excel(self.path, sheet_index)

