from django.urls import path

from books import views

urlpatterns = [
    path("borrow", views.borrow, name="borrow"),
    path("return", views.unborrow, name="unborrow"),
    path("all-books", views.all_books, name="all-books"),
    path("my-books", views.my_books, name="my-books")
]
