from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from vendors.models import Vendor

# Create your views here.
def all_vendors(request):
    vendors = list(Vendor.objects.all())

    context = {}
    context["vendors"] = vendors

    return render(request, "vendors/all-vendors.html", context=context)