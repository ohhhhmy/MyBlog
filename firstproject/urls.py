
from django.contrib import admin
from django.urls import path, include
import hello.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static

#20번째 줄 내용: settings.py에 작성한 url을 쓰겠다는 것

urlpatterns = [
    path('blog/<int:blog_id>', hello.views.detail, name="detail"),
    path('blog/create/', hello.views.create, name="create"),
    path('admin/', admin.site.urls),
    path('', hello.views.home, name='home'),
    path('newblog/', hello.views.blogposting, name = "newblog"),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
    path('accounts/', include('accounts.urls')),
    path('guestbook/bookings/', hello.views.bookings, name = "bookings"),
    path('guestbook/guestbook/', hello.views.guestbookpost, name = "guestbookpost"),
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#앱 만들고 임폿하는 것 잊지말기!
#url에 path 추가했다고 해서 무조건 html 띄우는게 아닙니다. path('blog/create/', hello.view.create 의 경우
#blog/create url이 들어오면 hello 안에 views 안에 create 함수를 실행시켜라 라는 의미입니다! url.py에 path 추가했다고 해서 html 무조건 띄우는거? 아님~
#궁금한 점: 포트폴리오는 왜 blog/porfolio/가 아니라 portfolio로 시작하나요?