from django import forms
from .models import Comment,Ad

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ('title','content','price','rubric','image',)

class WishForm(forms.Form):
    wish = forms.CharField()
    number = forms.CharField(max_length = 15)
