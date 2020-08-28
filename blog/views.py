from django.utils import timezone
from .models import Post, Item
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from django.http import HttpResponse


error = ""

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    items = Item.objects.all()
    return render(request, 'blog/index.html', {'items': items})

def post_list(request):
    posts = Post.objects.filter(start_date__lte=timezone.now()).order_by('start_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'tags' : ["Achievements","Education","Work Experience"]})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
def post_new(request):
    global error

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            error = ""
            if(post.start_date<= post.end_date):
                post.author = request.user
                # post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
            else:
                error = "Date invalid"

    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form,'error':error})

def post_edit(request, pk):
    global error

    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            error = ""
            if(post.start_date<= post.end_date):
                post = form.save(commit=False)
                post.author = request.user
                # post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
            else:
                error ="Date invalid"
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'error':error})

def post_delete(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect(post_list)