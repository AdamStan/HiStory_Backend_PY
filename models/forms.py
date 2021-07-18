from django.forms import ModelForm, BaseModelForm
from django.forms.fields import FileField
from django.forms.models import ModelFormMetaclass
from .models import Question

class QuestionForm(BaseModelForm, metaclass=ModelFormMetaclass):
    class Meta:
        model = Question
        fields = ["text", "correct_answer"]

    file = FileField(help_text="supported extensions are: .ods and .xlsx")


