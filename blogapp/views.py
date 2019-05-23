from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment
from django.utils import timezone
from django.core.paginator import Paginator

def home(request):
    blog_list = Blog.objects.all().order_by('-id')
    paginator = Paginator(blog_list, 5)
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    liked = Blog.objects.filter(user = request.user)
    return render(request, 'home.html', {'blogs':blogs, 'liked':liked})

def detail(request,detail_id):
    detail = get_object_or_404(Blog, pk=detail_id)
    comments = Comment.objects.filter(point = detail_id)
    return render(request, 'detail.html', {'detail':detail, 'comments':comments})

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

def writecomment(request, comment_id):
    comment = Comment()
    comment.writer = request.POST['writer']
    comment.content = request.POST['content']
    comment.point = get_object_or_404(Blog, pk=comment_id)
    comment.save()
    return redirect('/blog/detail/' + str(comment_id))

def like(request, like_id):
    user_like=get_object_or_404(Blog, pk=like_id)
    if user_like.user.filter(username=request.user.username).exists():
        user_like.user.remove(request.user)
    else:
        user_like.user.add(request.user)
    user_like.save()
    return redirect('/blog/detail/' + str(like_id))