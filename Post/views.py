from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views import generic
from Post.models import Post
from account.form import PostForm
from django.contrib import messages
# Create your views here.

# create post

def about(request):
    return render(request, 'post/about.html', {})

class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    login_url = '/login/'
    template_name = "post/post_form.html"
    redirect_field_name = "post/post_draft.html"
    form_class = PostForm


    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_draft')

class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    login_url ='/login/'
    redirect_field_name = 'post/post_detail.html'
    form_class = PostForm
   

    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': self.object.slug})


class PostDraftList(LoginRequiredMixin, generic.ListView):
    context_object_name = "posts"
    template_name = "post/post_draft.html"
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user, status=0).order_by('-create_on')


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy("home")


@login_required
def post_publish(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.publish()
    messages.success(request, 'You have successfully publish the post ')
    return redirect('home')
