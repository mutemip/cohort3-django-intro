from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .models import Post
from .forms import PostForm

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def about_us(request):
    return render(request, 'about.html', {})

def articles(request):
    posts = Post.objects.all() # select * from post
    context = {
        "posts": posts
        }
    return render(request, 'post.html', context)

def articles_details(request, pk):
    # post = Post.objects.get(pk=pk) # select * from post where id = pk
    post = get_object_or_404(Post, pk=pk)
    context = {
        "post": post
        }
    return render(request, 'post_details.html', context)

def article_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('articles'))
    else:
        form = PostForm()

    context = {
        "form": form
    }
    return render(request, 'create.html', context)

def article_update(request, pk):
    post_obj = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(instance=post_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('details', args=[pk, ]))
    else:
        form = PostForm(instance=post_obj)
    context = {
        "post_obj": post_obj,
        "form": form
        }
    return render(request, 'create.html', context)


def article_delete(request, pk):
    post_obj = get_object_or_404(Post, pk=pk)
    post_obj.delete()
    return redirect(reverse("articles"))

