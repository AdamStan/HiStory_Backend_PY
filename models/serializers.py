from rest_framework import serializers
from models.models import Category, AnswerType, Question, Answer


class AnswerTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnswerType
        fields = ["id", "type"]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "period", "details"]


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "text", "correct_answer"]

    correct_answer = serializers.SerializerMethodField('get_answer')

    def get_answer(self, question):
        return question.correct_answer.to_dict()


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "answer", "type", "category"]

    type = serializers.SerializerMethodField('get_type')
    category = serializers.SerializerMethodField('get_category')

    def get_type(self, answer):
        return answer.type.to_dict()

    def get_category(self, answer):
        return answer.category.to_dict()
