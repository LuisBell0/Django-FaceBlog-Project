from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('dashboard/create_post/',
         PostCreateView.as_view(),
         name="post-create"),
    path('post_like/<int:pk>/', like_post_view, name="post-like"),
    path('comment/<int:post_id>/', post_comments_list, name="comments"),
    path('comment/delete/<int:post_id>/<int:comment_id>/',
         comment_delete_function,
         name='comment-delete'),
    path('comment_like/<int:comment_id>/',
         like_comment_view,
         name="comment-like"),
    path('comment/<int:post_id>/<int:comment_id>/reply/',
         add_comment_reply,
         name='reply'),
    path('dashboard/update_post/<int:pk>/',
         PostUpdateView.as_view(),
         name="post-update"),
    path('dashboard/post_delete/<int:pk>/',
         PostDeleteView.as_view(),
         name="post-delete"),
    path('create_profile/', ProfileCreateView.as_view(),
         name='profile-create'),
    path('dashboard/edit_profile/<int:pk>/',
         ProfileUpdateFunction,
         name="profile-update"),
    path('accounts/login/', login_view, name='new_login'),
    path('search/profile/',
         search_profile,
         name='search-profile'),
    path('search/', handle_search, name='search'),
    path('<str:user_username>/',
         user_profile_view,
         name="user-profile"),
    path('follow/unfollow/<str:profile_id>/',
         follow_unfollow_profile,
         name='follow-unfollow'),
    path('<str:user_username>/followers/',
         followers_list_view,
         name='profile-followers'),
    path('<str:user_username>/following/',
         following_list_view,
         name='profile-following'),
]
