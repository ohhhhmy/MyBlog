from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from . import views
from .models import Blog, Guestbook
from django.core.paginator import Paginator
from .form import BlogPosting, Guestbookpost
# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def blogposting(request):
    if request.method == 'POST':
        form = BlogPosting(request.POST)
        if form.is_valid():
            posting = form.save(commit = False)
            posting.pub_date = timezone.now()
            posting.save()
            return redirect('home')
    
    else:
        form = BlogPosting()
        return render(request, 'new.html', {'form': form})


def bookings(request):
        bookings = Guestbook.objects
        return render(request, 'bookings.html', {'bookings':bookings})

def guestbookpost(request):
        if request.method == 'POST':
                form = Guestbookpost(request.POST)
                if form.is_valid():
                        bookposting = form.save(commit = False)
                        bookposting.pub_date = timezone.now()
                        bookposting.save()
                        return redirect('bookings')
        
        else:
                form = Guestbookpost()
                return render(request, 'guestbook.html', {'bookform':form})


#글쓰기 html을 띄우는게 목적이라면 form = BlogPost()는 왜 받아오나요?
#new.htm을 띄워 데이터를 받아와야 하는데 그 데이터를 담을(=GET) 통을 준비한다고 생각하면 된다.
#form이라는 key값을 통해 blogpost 하나하나를 관리할 수 있다.

#if request가 post라면 -> 블로그 포스트 함수를 받아 요청된 내용을 form안에 넣고


#URL은 항상 스트링이라 str써준 것! '/blog/'도 str형이니 str 더하기 str 더하기를 한 것!
#create는 사용자로부터 입력받은 내용을 DB에 넣어주는 함수