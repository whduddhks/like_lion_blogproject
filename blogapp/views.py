from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs':blogs})

def detail(request,detail_id):
    detail = get_object_or_404(Blog, pk=detail_id)
    return render(request, 'detail.html', {'detail':detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_post = Blog()
    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.body = request.POST['content']
    new_post.save()
    return redirect('/blog/detail/' + str(new_post.id))

def delete(request,delete_blog_id):
    delete_post = get_object_or_404(Blog, pk=delete_blog_id)
    delete_post.delete()
    return redirect('home')

def edit(request, edit_blog_id):
    edit_post = get_object_or_404(Blog, pk=edit_blog_id)
    return render(request, 'edit.html', {'detail':edit_post})

def update(request, update_blog_id):
    update_post = get_object_or_404(Blog, pk=update_blog_id)
    update_post.title = request.POST['title']
    update_post.writer = request.POST['writer']
    update_post.body = request.POST['content']
    update_post.save()
    return redirect('/blog/detail/' + str(update_blog_id))