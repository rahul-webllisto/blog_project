"""blog_project URL Configuration

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
from django.urls import path
from blog import views as blog_views
from accounts import views as acc_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.blog_list,name="blog-list"),
    path('<int:pk>/', blog_views.blog_detail,name="blog-detail"),
    path('create/', blog_views.create_blog,name="new-blog"),
    path('signup/', acc_views.sign_up,name="login"),
    path('addcomment/<pk>', blog_views.add_comment,name="add-comment"),

]
