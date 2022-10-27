from django.urls import path
from users import views

app_name = "users"
urlpatterns = [
    path("add-users", views.user_form, name="add-users"),
    path("show-data", views.show_data, name="show-data"),
]