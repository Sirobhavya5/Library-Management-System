import datetime
from dateutil.relativedelta import relativedelta

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from books.models import Book
from users.models import CustomUser
from books.forms import BorrowForm, UnborrowForm

# Create your views here.
def all_books(request):
    books = list(Book.objects.all())

    context = {}
    context["books"] = books

    return render(request, "books/all-books.html", context=context)

def my_books(request):
    if request.user.role == "1":
        books = list(Book.objects.filter(borrower__uuid=request.user.uuid))

        context = {}
        context["books"] = books

        return render(request, "books/my-books.html", context=context)
    else:
        return redirect("/")

@login_required
def borrow(request):
    if request.user.role == "2":
        if request.method == "POST":
            form = BorrowForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data["email"]
                title = form.cleaned_data["title"]

                Book.objects.filter(title=title).update(
                    status = "Borrowed",
                    borrower = CustomUser.objects.get(email=email),
                    borrow_date = datetime.datetime.now(),
                    return_date = datetime.datetime.now() + relativedelta(months=1),
                    charge = 0
                )

            return redirect("/")
        else:
            form = BorrowForm()
            return render(request, "books/borrow.html", {"form": form})
    else:
        return redirect("/")

@login_required
def unborrow(request):
    if request.user.role == "2":
        if request.method == "POST":
            form = UnborrowForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data["title"]

                Book.objects.filter(title=title).update(
                    status = "Available",
                    borrower = None,
                    borrow_date = None,
                    return_date = None,
                    charge = 0
                )
            
            return redirect("/")
        else:
            form = UnborrowForm()
            return render(request, "books/return.html", {"form": form})
    else:
        return redirect("/")
