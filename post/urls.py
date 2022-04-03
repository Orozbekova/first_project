from django.urls import path

from post.views import *



urlpatterns = [
    path('', PostCreateView.as_view()),
    path('post-list/<int:pk>/', PostListView.as_view()),
    path('post-update/<int:pk>/', PostUpdateView.as_view()),
    path('post-delete/<int:pk>/', PostDeleteView.as_view()),
]

