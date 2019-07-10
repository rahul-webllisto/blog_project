from django.urls import path
from blog import views


urlpatterns = [
    path('', views.blog_list_api, name="api-blog-list"),
    path('<int:pk>/', views.blog_detail_api, name="api-blog-detail"),
    path('add-comment/<int:pk>/', views.add_comment_api, name="api-add-comment"),
    path('edit-comment/<int:pk>/', views.edit_comment_api, name="api-edit-comment"),
]