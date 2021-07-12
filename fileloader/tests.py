from models.models import Answer, AnswerType, Category, Question
from fileloader.save import SaveQuestionsFromFile, TemporaryFileManager
import unittest
from django.test import TestCase
from fileloader.loaders import LoaderODS, LoaderXLSX
import os

class TestODSLoader(unittest.TestCase):

    def setUp(self):
        self.loader = LoaderODS("/home/adam/Projects/hi_story/fileloader/file.ods")
        self.loader.load()

    def test_ods_loader_questions(self):
        questions = self.loader.questions
        self.assertEqual(questions[0].text, "W których latach toczyła się pierwsza wojna punicka?")
        self.assertEqual(12, len(questions))


class TestXLSXLoader(unittest.TestCase):

    def setUp(self):
        self.loader = LoaderXLSX("/home/adam/Projects/hi_story/fileloader/file.ods")
        self.loader.load()

    def test_ods_loader_questions(self):
        questions = self.loader.questions
        self.assertEqual(questions[0].text, "W których latach toczyła się pierwsza wojna punicka?")
        self.assertEqual(12, len(questions))


class TemporaryFileManagerTests(unittest.TestCase):
    class MockFile:
        def __init__(self, file_name):
            self.name = file_name
        
        def chunks(self):
            return [bytes("abc", "utf-8"),]

    def test_save_and_remove_file(self):
        file = TemporaryFileManagerTests.MockFile("test.xlsx")
        PATH_TO_DOWNLOAD = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "download")

        manager = TemporaryFileManager(PATH_TO_DOWNLOAD, file)
        manager.save_file()
        temp_file_path = os.path.join(PATH_TO_DOWNLOAD, manager.temp_file_name + ".xlsx")
        print(temp_file_path)
        self.assertTrue(os.path.isfile(temp_file_path))
        manager.remove_file()
        self.assertFalse(os.path.isfile(temp_file_path))


class TestSavingQuestionsFromFile(TestCase):

    def setUp(self):
        self.loader = LoaderODS("/home/adam/Projects/hi_story/fileloader/file.ods")

    def test_questions_saving(self):
        SaveQuestionsFromFile(self.loader).save_questions()
        questions = Question.objects.all()
        answer_types = AnswerType.objects.all()
        categries = Category.objects.all()
        answers = Answer.objects.all()
        self.assertEqual(len(questions), len(self.loader.questions))
        self.assertEqual(2, len(answer_types), answer_types)
        self.assertEqual(1, len(categries), categries)
        # one answer is the same
        self.assertEqual(len(questions) - 1, len(answers))
    