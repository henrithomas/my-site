from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostsMonthView)
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='single-post'),
    path('post/<int:pk>/<slug:slug>/', PostDetailView.as_view(), name='single-post'),
    path('post/new/', PostCreateView.as_view(), name='create-post'),
    path('post/<int:pk>/<slug:slug>/update/', PostUpdateView.as_view(), name='update-post'),
    path('post/<int:pk>/<slug:slug>/delete/', PostDeleteView.as_view(), name='delete-post'),
    path('posts/<str:month>/', PostsMonthView.as_view(), name='month-post'),
    path('about/', views.about, name='blog-about'),
    path('photography/', views.photography, name='blog-photos'),
    path('projects/', views.projects, name='blog-projects'),
]
