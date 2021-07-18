from fileloader.loaders import LoaderFactory, LoaderXLSX, LoaderODS
from django.shortcuts import render

from django.shortcuts import render
from .forms import UploadFileForm
from .save import SaveQuestionsFromFile, TemporaryFileManager
import os

PATH_TO_DOWNLOAD = os.path.join(os.path.dirname(os.path.realpath(__file__)), "download")


def upload_file(request):
    data_added = ""
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            upload_file = request.FILES['file']
            handle_uploaded_file(upload_file)
            data_added = "The file was loaded succesfully."
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {"form": form, "message_succ": data_added})


def handle_uploaded_file(file):
    manager = TemporaryFileManager(PATH_TO_DOWNLOAD, file)
    path_to_temp_file = manager.save_file()
    try:
        loader = LoaderFactory.create_loader(path_to_temp_file)
        SaveQuestionsFromFile(loader).save_questions()
    finally:
        manager.remove_file()

