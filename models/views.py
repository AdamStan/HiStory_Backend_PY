from fileloader.views import handle_uploaded_file
from fileloader.forms import UploadFileForm
from django.shortcuts import render

# Create your views here.
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
    return render(request, 'uploaded.html', {"form": form, "message_succ": data_added})

