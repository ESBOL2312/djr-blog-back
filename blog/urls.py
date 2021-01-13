from django.urls import path
from blog import views

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:pk>/', views.article_detail),
    path('categories/', views.category_list),
    path('categories/<int:pk>/', views.category_articles),
    #path('ar/<int:pk>/', views.article_detail)
]