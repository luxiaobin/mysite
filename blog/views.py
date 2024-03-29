from django.shortcuts import render
from django.template import loader, Context
from blog.models import BlogPost
from django.http import HttpResponse

# Create your views here.

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("archive.html")
    c = Context({ 'posts': posts})
    return HttpResponse(t.render(c))