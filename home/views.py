import re
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login


from .models import *
from .forms import *

# Create your views here.




class Home(ListView):
    model = Article
    template_name = 'home/home.html'
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context





# Детально каждая статья + Форма для комментов
class ArticleDetail(FormMixin, DetailView):
    model = Article
    template_name = 'home/article_detail.html'
    pk_url_kwarg = 'article_pk'
    context_object_name = 'article'
    form_class = CommentForm
    success_msg = 'Комментарий создан!'

    # data, которая передается в шаблон 
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        data = {
            'comments': Comment.objects.filter(article_id=context['article'].pk), #Комментарии только к нашему посту
        }
        

        for obj in data:
            context[obj] = data[obj]
        return context






                #Создание Формы для комментариев 👇👇

    #обработка post запроса (из-за того что is_valid Не сохраняет форму, мы создаем функцию form_valid, чтобы ее сохранить)
    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():   #Проверяем форму на валидность
            return self.form_valid(form)
        else: 
            return self.form_invalid(form)


    #Сохраняем форму
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()   #Указываем в ForeingKey наш объект.
        self.object.comment_author = self.request.user
        self.object.save()

        return super().form_valid(form)



    #Определяем куда направлятся после отправки формы
    def get_success_url(self, **kwargs):
        return reverse_lazy('article_detail', kwargs={'article_pk': self.get_object().id}) #Как в get_absolute_url()




#Форма создания Статей
class NewArticle(CreateView):
    form_class = NewArticleForm
    template_name: str = 'home/newArticle.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)


        data = {
            1: '1'
        }
        

        for obj in data:
            context[obj] = data[obj]
        return context


    #обработка post запроса (из-за того что is_valid Не сохраняет форму, мы создаем функцию form_valid, чтобы ее сохранить)
    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():   #Проверяем форму на валидность
            return self.form_valid(form)
        else: 
            return self.form_invalid(form)


    #Сохраняем форму
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()

        return super().form_valid(form)







# Регистрация Пользователя
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'home/register.html'
    success_url = reverse_lazy('home')    #!!!!!!!!


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        data = {
            1: '1'
        }
        

        for obj in data:
            context[obj] = data[obj]
        return context



    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')





# Авторизация пользователя
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'home/login.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        data = {
                1: '1'
            }
            
        for obj in data:
            context[obj] = data[obj]
        return context


    
    def get_success_url(self):
        return reverse_lazy('home')





# Выход с аккаунта
def logout_user(request):
    logout(request)
    return redirect('home')

