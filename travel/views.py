from django.shortcuts import render


def home(req):
    name = "3.14dor"
    return render(req, "home.html", {"name": name})
