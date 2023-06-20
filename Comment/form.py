from Comment.models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets={
            'name':forms.TextInput(attrs={'class':'textinputclass'}),
            'body':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }