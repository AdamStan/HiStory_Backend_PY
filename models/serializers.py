from rest_framework import serializers
from models.models import Category, AnswerType, Question, Answer


class AnswerTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnswerType
        fields = ["id", "type"]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "category"]


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
