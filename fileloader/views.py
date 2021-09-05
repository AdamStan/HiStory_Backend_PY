from fileloader.loaders import LoaderFactory, LoaderXLSX, LoaderODS
from django.shortcuts import render

from django.shortcuts import render
from .forms import UploadFileForm
from .save import SaveQuestionsFromFile, TemporaryFileManager
import os

PATH_TO_DOWNLOAD = os.path.join(os.path.dirname(os.path.realpath(__file__)), "download")


def handle_uploaded_file(file):
    manager = TemporaryFileManager(PATH_TO_DOWNLOAD, file)
    path_to_temp_file = manager.save_file()
    try:
        loader = LoaderFactory.create_loader(path_to_temp_file)
        SaveQuestionsFromFile(loader).save_questions()
    finally:
        manager.remove_file()

