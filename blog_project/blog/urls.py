from django.urls import path
from blog import views


urlpatterns = [    
    path('', views.blog_list_api,name="api-blog-list"),
    path('<int:pk>/', views.blog_detail_api,name="api-blog-detail"),
]