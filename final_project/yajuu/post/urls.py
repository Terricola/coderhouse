from django.urls import path

from post import views

app_name = "post"
urlpatterns = [
    #path("post/list", views.post_list, name="post-list"),
    
    path("add-post", views.post_form, name="add-post"), 
    path("posts/", views.PostListView.as_view(), name="post-list"),     
    path("post/<int:pk>/detail/", views.PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),
    path("comment/<int:pk>/add/", views.CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),
]