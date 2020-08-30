from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    path('cv', views.cv_list, name='cv_list'),
    path('cv/<int:pk>/', views.cv_detail, name='cv_detail'),
    path('cv/new/', views.cv_new, name='cv_new'),
    path('cv/<int:pk>/edit/', views.cv_edit, name='cv_edit'),
    path('cv/<int:pk>/delete/', views.cv_delete, name='cv_delete'),
    path('blog', views.blog_list, name='blog_list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/new/', views.blog_new, name='blog_new'),
    path('blog/<int:pk>/edit/', views.blog_edit, name='blog_edit'),
    path('blog/<int:pk>/delete/', views.blog_delete, name='blog_delete')

]