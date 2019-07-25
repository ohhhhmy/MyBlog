"""sociallogin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import loginapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginapp.views.home, name = 'home'),
    path('accounts/', include('allauth.urls')),

]

#프로젝트 따로 만드는 이유는? 꼬일까봐
#path에서 accounts는 만들어놓은 앱을 의미하나요? 아니다 구글의 accounts를 가져온 것
#새로 만든 user는 loginapp내 home에 접근하기 위한 admin 계정인가요? 프로젝트별로 사이트 관리자를 만드는 것. 