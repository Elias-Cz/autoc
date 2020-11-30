
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import Customer

# Create your views here.
def index(request):
    custs = Customer.objects.all()
    return render(request, "autocom/index.html", {
    "custs": custs
    })

def my_resp(request):
    mylist = []
    custs = Customer.objects.all()
    print(custs)
    for c in custs:
        first = c.first_name

        mylist.append(first)

    return JsonResponse({
    "custs": mylist
    })
