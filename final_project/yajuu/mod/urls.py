from django.urls import path
from mod import views

app_name = "mod"
urlpatterns = [
    path("add-mod", views.mod_form, name="add-mod"),
    path("login", views.login_request, name="login"),
    path("register", views.register, name="register"),
]