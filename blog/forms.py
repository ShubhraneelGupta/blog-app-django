from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'border rounded-xl p-2 w-96'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'border rounded-xl p-2 w-96'}))
    to = forms.EmailField(widget=forms.TextInput(attrs={'class': 'border rounded-xl p-2 w-96'}))
    comments = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'border rounded-xl p-2 w-96'}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border border-gray-300 p-2 my-2 rounded w-1/2'}),
            'email': forms.EmailInput(attrs={'class': 'border border-gray-300 p-2 my-2 rounded w-1/2'}),
            'body': forms.Textarea(attrs={'class': 'border border-gray-300 p-2 my-2 rounded w-1/2'}),
        }
class SearchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500'}))