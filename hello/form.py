from django import forms
from .models import Blog, Guestbook

class BlogPosting(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body']

class Guestbookpost(forms.ModelForm):
    class Meta:
        model = Guestbook
        fields = ['nickname', 'title', 'body']








    
#class로 정의한 model Blog 안에 BlogPost라는 또다른 class를 정의한다! 
