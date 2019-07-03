from django.urls import path
from blog import views


urlpatterns = [    
    path('', views.blog_list_api,name="api-blog-list"),
    path('<int:pk>/', views.blog_detail_api,name="api-blog-detail"),
    path('addcomment/<int:pk>/', views.add_comment_api,name="api-add-comment"),
    # path('<int:pk>/<int:pk>/', views.add_comment_api,name="api-add-comment"),
]