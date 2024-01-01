from django.shortcuts import render
from .models import Post

# Create your views here.
def blog(request):
    allPosts =  Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blog.html', context)

def blog_post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context= {'post': post}
    return render(request, 'blog-post.html', context)