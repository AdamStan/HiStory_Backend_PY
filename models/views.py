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
    queryset = AnswerType.objects.all()
    serializer_class = AnswerTypeSerializer
    permission_classes = [permissions.AllowAny]


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']

    def get_queryset(self):
        queryset = self.queryset

        type_name = self.request.query_params.get("type")
        if type_name:
            queryset = queryset.filter(type__type=type_name)

        category_name = self.request.query_params.get("category")
        if category_name:
            queryset = queryset.filter(category__category=category_name)

        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']

    def get_queryset(self):
        category_name = self.request.query_params.get("category")
        if category_name:
            return self.queryset.filter(category=category_name)
        return self.queryset


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']

    def get_queryset(self):
        queryset = self.queryset
        categories = self.request.query_params.getlist("category")
        print(categories)
        if categories:
            queryset = self.queryset.filter(correct_answer__category__category__in=categories)
        return queryset
