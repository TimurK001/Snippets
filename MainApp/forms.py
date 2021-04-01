from django.forms import ModelForm, TextInput
from MainApp.models import Snippet


class SnippetForm(ModelForm):
   class Meta:
       model = Snippet
       # Описываем поля, которые будем заполнять в форме
       fields = ['name', 'lang', 'code', 'public']
       widgets = {
           "name":TextInput(attrs={'class':'my-class', "placeholder":"Название сниппета"})
       }