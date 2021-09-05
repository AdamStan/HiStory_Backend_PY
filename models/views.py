from fileloader.views import handle_uploaded_file
from fileloader.forms import UploadFileForm


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            file_to_upload = request.FILES['file']
            handle_uploaded_file(file_to_upload)
            return True
    return False

