from django.urls import path
from family_data import views

# This is not working correctly:
# app_name = "family_data"
# urlpatterns = [
#     path("add-data", views.add_data),
#     path("show-data", views.show_data),
# ]