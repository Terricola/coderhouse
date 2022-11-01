from django.urls import path
from post import views

app_name = "post"
urlpatterns = [
    path("add-post", views.post_form, name="add-post"),
    path("post-detail", views.post_detail, name="post-detail"),
]