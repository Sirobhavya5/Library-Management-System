from django.urls import path

from libraries import views

urlpatterns = [
    path("all-libraries", views.all_libraries, name="all-libraries"),
    path("my-libraries", views.my_libraries, name="my-libraries")
]
