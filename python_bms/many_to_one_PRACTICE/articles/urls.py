from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/comment_create/', views.comment_create, name='comment_create'), 
    path('<int:article_pk>/comment_delete/<int:comment_pk>/', views.comment_delete, name='comment_delete'), 
]
