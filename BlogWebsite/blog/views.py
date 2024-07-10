from django.http import HttpResponse
from django.template import loader
from .models import User, Post, Comment, Category

def users(request):
    users = User.objects.all().values()
    template = loader.get_template('users.html')
    context = {
        'users': users,
    }
    return HttpResponse(template.render(context, request))

def posts(request):
    posts = Post.objects.all().values()
    template = loader.get_template('blogs.html')
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))

def comments(request):
    comments = Comment.objects.select_related('post').all()
    template = loader.get_template('comments.html')
    context = {
        'comments': comments,
    }
    return HttpResponse(template.render(context, request))

def categories(request):
    categories = Category.objects.all().values()
    template = loader.get_template('categories.html')
    context = {
        'categories': categories,
    }
    return HttpResponse(template.render(context, request))

def blog_details(request, id):
    post = Post.objects.get(id=id)
    template = loader.get_template('blogdetails.html')
    context = {
        'post': post,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())