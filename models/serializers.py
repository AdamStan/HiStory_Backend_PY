import json

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
        fields = ["id", "text", "correct_answer"]


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.SerializerMethodField('get_type')
    category = serializers.SerializerMethodField('get_category')

    class Meta:
        model = Answer
        fields = ["id", "answer", "type", "category"]

    def get_type(self, answer):
        return answer.type.to_dict()

    def get_category(self, answer):
        return answer.category.to_dict()
