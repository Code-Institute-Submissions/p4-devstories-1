from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('blog/', views.create_post, name='create_post'),
    path('blog/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('blog/<int:blog_post_id>/',
         views.PostDetail.as_view(), name='blog_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('blog/delete/<int:blog_post_id>',
         views.delete_post, name='delete_post'),
    path('blog/<slug:slug>/update/', views.update_post, name='update_post'),
    path('newsletter/subscribe', views.subscribe, name='subscribe'),
    path('newsletter/unsubscribe', views.unsubscribe, name='unsubscribe'),
    path('newsletter/update', views.editemail, name='editemail'),
]
