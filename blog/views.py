from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.


class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "base.html"
    paginate_by = 6
