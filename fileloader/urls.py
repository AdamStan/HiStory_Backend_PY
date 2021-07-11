from django.urls import path
from . import views

app_name = 'fileloader'

urlpatterns = [
    path('import_questions', views.upload_file, name='import_questions'),
]