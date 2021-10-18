from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.


def home(request):
    # GET.get("q")
    # COOKIES
    # method
    # if request.method=="GET":
    #     print(f"you are using {request.method} method")
    # print(request.META)

    context = {
        "title": "clarusway",
        "dict1": {"django": "best framework"},
        "my_list": [2, 3, 4],
    }

    return render(request, "app/home.html", context)
