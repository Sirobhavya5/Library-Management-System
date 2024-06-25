from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from libraries.models import Library

# Create your views here.
def all_libraries(request):
    libraries = list(Library.objects.all())

    context = {}
    context["libraries"] = libraries

    return render(request, "libraries/all-libraries.html", context=context)

def my_libraries(request):
    if request.user.role == "3":
        libraries = list(Library.objects.filter(owner__uuid=request.user.uuid))

        context = {}
        context["libraries"] = libraries

        return render(request, "libraries/my-libraries.html", context=context)
    else:
        return redirect("/")