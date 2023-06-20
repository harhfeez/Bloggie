from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from Comment.form import CommentForm
from Post.models import Post
from django.contrib import messages
# Create your views here.
@login_required

def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            
            # Save the comment to the database
            post.comment_count += 1
            comment.save()
            messages.success(request, 'Your comment got posted successfully!')
            return redirect('post_detail', slug=slug)
    else:
        comment_form = CommentForm()

    return render(request, 'post/post_detailhtml', {'comment_form': comment_form})