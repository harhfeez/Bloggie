from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import get_user_model
from Post.models import Post

User = get_user_model()

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2' )

        widgets= {
            'username': forms.TextInput(attrs={'class': 'textinputclass'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),

        }

class SignInForm(forms.Form):
    # class Meta:
    #     model = User
    #     fields = ('username', 'password1')

    #     widgets = {
    #         'username': forms.TextInput(attrs={'class': 'form-control'}),
    #         'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
    #     }

    username = forms.CharField(max_length=250, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ( 'title','content')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'content':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent' }),

        }