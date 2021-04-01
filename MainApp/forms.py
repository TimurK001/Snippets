from django.forms import ModelForm, TextInput, EmailField
from MainApp.models import Snippet, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SnippetForm(ModelForm):
   class Meta:
       model = Snippet
       # Описываем поля, которые будем заполнять в форме
       fields = ['name', 'lang', 'code', 'public']
       widgets = {
           "name":TextInput(attrs={'class':'my-class', "placeholder":"Название сниппета"})
       }

class RegForm(UserCreationForm):
   email = EmailField()
   class Meta:
       model = User
       fields = ['username', 'email', 'password1', 'password2']

class CommentForm(ModelForm):
   class Meta:
       model = Comment
       # Описываем поля, которые будем заполнять в форме
       fields = ['text']
