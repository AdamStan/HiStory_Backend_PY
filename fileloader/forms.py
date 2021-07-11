from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, *kwargs)
        self.fields['file'].help_text = "supported extensions are: .ods and .xlsx"

