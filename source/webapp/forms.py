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
class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")
#
#
# class FileForm(forms.ModelForm):
#
#     class Meta:
#         model = File
#         fields = ['name', 'file']
