from django.shortcuts import render, redirect, get_object_or_404
from Comment.form import CommentForm
from django.contrib.auth import logout, login, authenticate
from account.form import SignUpForm,SignInForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from Post.models import Post
from django.views import generic
from django.core.paginator import Paginator
from django.contrib import messages
from Comment.models import Comment
from django.db.models import Count


# Create your views here.
class PostHome(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-create_on')
    context_object_name = "posts"
    template_name = "home.html"
    paginate_by = 4

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(comment_count=Count('comment'))
        return queryset




# def index(request):
#     posts = Post.objects.filter(status=1).order_by('-create_on')  # Retrieve all blog posts, ordered by the latest first
#     paginator = Paginator(posts, 4)  # Create a paginator with 4 posts per page
#     page_number = request.GET.get('page')  # Get the current page number from the query parameters
#     page_obj = paginator.get_page(page_number)  # Get the Page object for the current page

#     return render(request, 'home.html', {'page_obj': page_obj})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post)
        # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            
            # Save the comment to the database
            comment.save()
            messages.success(request, 'Your comment got posted successfully!')
            return redirect('post_detail', slug=slug)
    else:
        comment_form = CommentForm()

    return render(request, "post/post_detail.html", {'post': post,
                                           'comments': comments,
                                           'comment_form': comment_form})
   


# Registration

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account was created successfully ')
                return redirect('signin')
            else:
                messages.error(request, "Registration wasn't Successful....")
                print("password is not strong")
                return redirect('register')

        else:
            form = SignUpForm()
            return render(request, 'account/register.html', {'form': form})
    


def sign_in(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You are now logged in')
                return redirect('home')
            else:
                messages.error(request, "error signing in..." )
                return redirect('register')
        else:
            messages.error(request, 'Your username or password is not correct...')
            print('Your username or password is not correct...')
            return redirect('signin')
        
    else:
        form = SignInForm()
        return render(request, "account/signin.html", {'form':form})
        



def sign_out(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('home')
    