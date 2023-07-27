from pyexpat import model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from .models import *





# Форма комментария
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'}),
        }
        


    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if len(title) > 200:
    #         raise ('Превышает 200 симв.')
    #     return title


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label = 'Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label = 'Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label = 'Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    # Эти переменные уже были такими, но мы их перезаписали, чтобы добавить Widjets (Кроме widjets все было точно таким же(В UserCreationForm))
    # Можно это и не писать!

    

    class Meta:
        model = User
        fields = ('username','first_name', 'password1', 'password2')





class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))




class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'text', 'image')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)