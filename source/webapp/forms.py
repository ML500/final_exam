from django import forms

#
# from webapp.models import File
#
# BROWSER_DATETIME_FORMAT = '%d.%m.%Y %H:%M'
#
#
# class XDatepickerWidget(forms.TextInput):
#     template_name = 'widgets/xdatepicker_widget.html'
#
#
from webapp.models import Message


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']
#
#
# class FileForm(forms.ModelForm):
#
#     class Meta:
#         model = File
#         fields = ['name', 'file']
