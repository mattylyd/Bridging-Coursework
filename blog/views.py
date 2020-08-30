from django.utils import timezone
from .models import CV, Blog
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CVForm,BlogForm
from django.http import HttpResponse


error = ""

def home_page(request):
    return render(request, 'blog/index.html')

def cv_list(request):
    posts = CV.objects.filter(start_date__lte=timezone.now()).order_by('start_date')
    return render(request, 'blog/cv_list.html', {'posts': posts, 'tags' : ["About Me","Achievements","Education","Work Experience"]})

def cv_detail(request, pk):
    post = get_object_or_404(CV, pk=pk)
    return render(request, 'blog/cv_detail.html', {'post': post})
def cv_new(request):
    global error

    if request.method == "POST":
        form = CVForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            error = ""
            if(post.start_date<= post.end_date):
                post.author = request.user
                # post.published_date = timezone.now()
                post.save()
                return redirect('cv_detail', pk=post.pk)
            else:
                error = "Date invalid"

    else:
        form = CVForm()
    return render(request, 'blog/cv_edit.html', {'form': form, 'error':error})

def cv_edit(request, pk):
    global error

    post = get_object_or_404(CV, pk=pk)
    if request.method == "POST":
        form = CVForm(request.POST, instance=post)
        if form.is_valid():
            error = ""
            if(post.start_date<= post.end_date):
                post = form.save(commit=False)
                post.author = request.user
                # post.published_date = timezone.now()
                post.save()
                return redirect('cv_detail', pk=post.pk)
            else:
                error ="Date invalid"
    else:
        form = CVForm(instance=post)
    return render(request, 'blog/cv_edit.html', {'form': form, 'error':error})

def cv_delete(request,pk):
    post = get_object_or_404(CV, pk=pk)
    post.delete()
    return redirect(cv_list)

def blog_list(request):
    blogs = Blog.objects.filter(datetime__lte=timezone.now()).order_by('datetime')
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog})
def blog_new(request):

    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.datetime = timezone.now()
            blog.save()
            print("yes!")
            return redirect('blog_detail', pk=blog.pk)

    else:
        form = BlogForm()
    return render(request, 'blog/blog_edit.html', {'form': form})

def blog_edit(request, pk):

    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog.datetime = timezone.now()
            blog.save()
            return redirect('blog_detail', pk=blog.pk)

    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/blog_edit.html', {'form': form})

def blog_delete(request,pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect(blog_list)