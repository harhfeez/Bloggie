from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('about', views.about, name='about'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<str:slug>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<str:slug>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/draft/', views.PostDraftList.as_view(),name='post_draft'),
    path('post/<str:slug>/publish/', views.post_publish,name='post_publish'),
 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


