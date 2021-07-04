from models.models import Answer, AnswerType, Category, Question
from fileloader.save import SaveQuestionsFromFile
import unittest
from django.test import TestCase
from fileloader.ods_loader import LoaderODS


class TestODSLoader(unittest.TestCase):

    def setUp(self):
        self.loader = LoaderODS("/home/adam/Projects/hi_story/fileloader/file.ods")
        self.loader.load()

    def test_ods_loader_questions(self):
        questions = self.loader.questions
        self.assertEqual(questions[0].text, "W których latach toczyła się pierwsza wojna punicka?")
        self.assertEqual(12, len(questions))


class TestSavingQuestionsFromFile(TestCase):

    def setUp(self):
        loader = LoaderODS("/home/adam/Projects/hi_story/fileloader/file.ods")
        loader.load()
        self.questions = loader.questions

    def test_questions_saving(self):
        SaveQuestionsFromFile(self.questions).save_questions()
        questions = Question.objects.all()
        answer_types = AnswerType.objects.all()
        categries = Category.objects.all()
        answers = Answer.objects.all()
        self.assertEqual(len(questions), len(self.questions))
        self.assertEqual(2, len(answer_types), answer_types)
        self.assertEqual(1, len(categries), categries)
        # one answer is the same
        self.assertEqual(len(questions) - 1, len(answers))
    