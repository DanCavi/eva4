from django.urls import path
from . import views

urlpatterns = [
    path('', views.renderPosts, name = 'renderPosts'),
    path('<int:post_id>', views.post_detail, name = 'post_detail'),
]
