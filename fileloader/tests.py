from fileloader.help import get_extension
from models.models import Answer, AnswerType, Category, Question
from fileloader.save import SaveQuestionsFromFile, TemporaryFileManager
import unittest
from django.test import TestCase
from fileloader.loaders import LoaderFactory, LoaderODS, LoaderXLSX
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
        categories = Category.objects.all()
        answers = Answer.objects.all()
        self.assertEqual(len(questions), len(self.loader.questions))
        self.assertEqual(2, len(answer_types), answer_types)
        self.assertEqual(1, len(categories), categories)
        # one answer is the same
        self.assertEqual(len(questions) - 1, len(answers))
    

class TestGetExtension(unittest.TestCase):

    def test_get_extension_1(self):
        file_name = "super.ext"
        extension = get_extension(file_name)
        self.assertEqual("ext", extension)

    def test_get_extension_2(self):
        file_name = "super.ext.xlsx"
        extension = get_extension(file_name)
        self.assertEqual("xlsx", extension)

    def test_get_extension_3(self):
        linux_path = "/super/folder/name/super.ext"
        extension = get_extension(linux_path)
        self.assertEqual("ext", extension)

    def test_get_extension_4(self):
        windows_path = "C:\\super\\folder\\name\\super.ext"
        extension = get_extension(windows_path)
        self.assertEqual("ext", extension)


class TestLoaderFactory(unittest.TestCase):

    def test_loader_not_supported_extension(self):
        file_name = "super.ext"
        self.assertRaises(ValueError, LoaderFactory.create_loader, file_name)

    def test_loader_xlsx(self):
        file_name = "super.xlsx"
        loader = LoaderFactory.create_loader(file_name)
        self.assertIsInstance(loader, LoaderXLSX)

    def test_loader_ods(self):
        file_name = "super.ods"
        loader = LoaderFactory.create_loader(file_name)
        self.assertIsInstance(loader, LoaderODS)
