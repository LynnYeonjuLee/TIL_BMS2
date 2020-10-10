from django.urls import path, include
from . import views

app_name='community'
urlpatterns = [
    path('', views.review_list, name='review_list'), 
    path('create/', views.review_create, name='review_create'), 
    path('<int:review_pk>/', views.review_detail, name='review_detail'), 
    path('<int:review_pk>/comments/', views.comments_create, name='comments_create'), 
    path('<int:review_pk>/comments/<int:comment_pk>/', views.comments_delete, name='comments_delete'), 
    path('<int:review_pk>/like/', views.like, name='like'),
    
    path('<int:user_pk>/review_list/', views.person_review_list, name='person_review_list')
]