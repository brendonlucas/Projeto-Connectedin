from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

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

    else:
        return redirect('index')


@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect('index')

@login_required
def comment_post(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        post = Post.objects.get(id=post_id)
        
        if form.is_valid():
            data_form = form.cleaned_data
            Post.objects.create(content=data_form['content'], user=request.user, type_post='1', commented_post=post)

            return redirect('index')
        else:
            return redirect('index')               

    else:
        return redirect('index')
