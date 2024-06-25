from django.urls import path

from vendors import views

urlpatterns = [
    path("all-vendors", views.all_vendors, name="all-vendors"),
]
