from fileloader.views import handle_uploaded_file
from fileloader.forms import UploadFileForm
from rest_framework import viewsets
from rest_framework import permissions

from models.models import AnswerType, Answer, Category, Question
from models.serializers import AnswerTypeSerializer, AnswerSerializer, QuestionSerializer, CategorySerializer


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            file_to_upload = request.FILES['file']
            handle_uploaded_file(file_to_upload)
            return True
    return False


class AnswerTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AnswerType.objects.all()
    serializer_class = AnswerTypeSerializer
    permission_classes = [permissions.AllowAny]


class AnswerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.AllowAny]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.AllowAny]
