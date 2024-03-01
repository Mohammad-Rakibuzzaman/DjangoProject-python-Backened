from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
# Create your views here.
#def home(request):
#    return render(request, 'home.html')
class home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_blog.html'
    #fields = '__all__'
    #fields = ('title','title_tag','author', 'body')
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"
    #fields = ['title', 'title_tag', 'body']




    
def privacy(request):
    return render(request, 'privacy.html')
def laptop(request):
    return render(request, 'laptop.html')
def document(request):
    return render(request, 'documentation.html')