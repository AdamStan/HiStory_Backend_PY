from django.urls import path, include
from models import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'answer_types', views.AnswerTypeViewSet)
router.register(r'answers', views.AnswerViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
