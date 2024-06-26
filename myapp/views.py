from django.shortcuts import render, get_object_or_404, redirect
from myadminapp.models import sliderdata, offerdata
from myadminapp.models import blogdata
from myapp.models import CommentForm , Comment
from myadminapp.models import categorydata, blogdata


# Create your views here.

def indexpage(request):

    slider_data = sliderdata.objects.all()
    weoffer_data = offerdata.objects.all()
    blog_data = blogdata.objects.all()

    return render(request, "index.html" , {'slider_data': slider_data, 'offerdata': weoffer_data, 'blog_data': blog_data})

def contactpage(request):
    return render(request, 'contact.html')

def aboutpage(request):
    return render(request, "about.html")

def bloggridpage(request):
    return render(request, 'blog-grid.html')

def blogsinglepage(request, pk):
    blog_post = get_object_or_404(blogdata, pk=pk)

    comments = blog_post.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog_post = blog_post
            new_comment.save()
            return redirect('blogsingle', pk=blog_post.pk)
    else:
        comment_form = CommentForm()

    # Get the previous blog post
    prev_post = blogdata.objects.filter(pk__lt=blog_post.pk).order_by('-pk').first()
    # Get the next blog post
    next_post = blogdata.objects.filter(pk__gt=blog_post.pk).order_by('pk').first()

    recent_posts = blogdata.objects.order_by('-post_date')[:3]
    return render(request, 'blog-single.html', {'blog_post': blog_post ,'comments': comments,
        'comment_form': comment_form, 'recent_posts': recent_posts, 'prev_post': prev_post, 'next_post': next_post})

def blogpage(request):
    return render(request, "blog.html")

def clientspage(request):
    return render(request, 'clients.html')

def index2page(request):
    return render(request, 'index-2.html')

def popoverpage(request):
    return render(request, 'popover requires tooltip.html')

def servicespage(request):
    return render(request, 'services.html')

def singleproject(request):
    return render(request, 'single-project.html')

def tweenlite(request):
    return render(request, 'TweenLite.html')

def columnthree(request):
    categories = categorydata.objects.all()
    blogs = blogdata.objects.all()
    return render(request, 'work-3columns.html', {'categories': categories, 'blogs': blogs})

def columnfour(request):
    return render(request, 'work-4columns.html')