from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            data_form = form.cleaned_data
            Post.objects.create(image=data_form['image'], content=data_form['content'], user=request.user)

            return redirect('index')

    else:
        return redirect('index')


@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id, user=request.user)
    post.delete()

    return redirect('index')