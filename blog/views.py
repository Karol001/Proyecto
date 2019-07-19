from django.shortcuts import render
from .models import Post
from django.core.files.storage import FileSystemStorage
import os


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)



