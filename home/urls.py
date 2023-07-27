from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('articles/<int:article_pk>', views.ArticleDetail.as_view(), name='article_detail'),
    path('articles/newArticle', views.NewArticle.as_view(), name='new_article'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name = 'login'),
    path('logout/', views.logout_user, name='logout')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)