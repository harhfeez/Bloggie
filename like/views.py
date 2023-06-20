from django.shortcuts import render
from like.models import Like
from Post.models import Post
# Create your views here.
from django.shortcuts import get_object_or_404, redirect

def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    user = request.user
    existing_like = Like.objects.filter(user=user, post=post).first()

    if existing_like:
        existing_like.delete()
        post.like_count -= 1
    else:
        Like.objects.create(user=user, post=post)
        post.like_count += 1

    post.save()
    return redirect('post_detail', slug=slug)

