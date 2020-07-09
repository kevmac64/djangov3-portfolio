from django.shortcuts import render, get_object_or_404
from .models import Blog


# Create your views here.
def all_blogs(request):
    #blogs = Blog.objects.all()
    blogs = Blog.objects.order_by('-date')  #for sorting
    #Blog.objects.order_by('-date')[:5] for the last 5

    return render(request, 'blog/all_blogs.html', {
        'blogs': blogs,
    })

def detail(request, blog_id):
    the_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {
        'blog': the_blog,
    })