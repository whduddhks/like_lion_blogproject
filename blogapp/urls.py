from django.contrib import admin
from django.urls import path
from blogapp import views

urlpatterns = [
    path('detail/<int:detail_id>', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('delete/<int:delete_blog_id>', views.delete, name="delete"),
    path('edit/<int:edit_blog_id>', views.edit, name="edit"),
    path('update/<int:update_blog_id>', views.update, name="update"),
    path('writecomment/<int:comment_id>', views.writecomment, name="writecomment"),
    path('like/<int:like_id>', views.like, name="like"),
]