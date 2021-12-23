from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('published/', views.pub_post_list, name="pub_post_list"),
    path('unpublished/', views.draft_post_list, name="draft_post_list"),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('post/<slug:s>/', views.post_detail_slug, name='post_detail_slug'),
]

