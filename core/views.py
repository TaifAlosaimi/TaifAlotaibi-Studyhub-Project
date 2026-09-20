from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from .forms import FeedbackForm

def get_theme(request):
    theme = request.COOKIES.get("theme", "light")

    if theme not in ["light", "dark"]:
        theme = "light"

    return theme

resources = [
    {
        "id": 1,
        "title": "Introduction to Python",
        "type": "Article",
        "description": "A beginner-friendly introduction to Python programming.",
        "url": "https://www.python.org/about/gettingstarted/",
    },
    {
        "id": 2,
        "title": "Django Fundamentals",
        "type": "Course",
        "description": "Learn the fundamentals of building web applications with Django.",
        "url": "https://www.djangoproject.com/start/",
    },
    {
        "id": 3,
        "title": "Python Documentation",
        "type": "Documentation",
        "description": "Official documentation and reference for the Python programming language.",
        "url": "https://docs.python.org/3/",
    },
    {
        "id": 4,
        "title": "Django Tutorial",
        "type": "Article",
        "description": "A practical tutorial for learning the basics of Django.",
        "url": "https://docs.djangoproject.com/en/6.1/intro/tutorial01/",
    },
]


def home(request):
    context = {
        "theme": get_theme(request),
    }

    return render(request, "core/home.html", context)


def resource_list(request):
    context = {
        "resources": resources,
        "theme": get_theme(request),
    }

    return render(request, "core/resource_list.html", context)



def resource_detail(request, id):
    resource = next(
        (resource for resource in resources if resource["id"] == id),
        None,
    )

    if resource is None:
        raise Http404("Resource not found")

    tab = request.GET.get("tab", "overview")

    
    context = {
        "resource": resource,
        "tab": tab,
        "theme": get_theme(request),

    }

    return render(request, "core/resource_detail.html", context)



def add_favorite(request, id):
    favorite_ids = request.session.get("favorites", [])

    if id not in favorite_ids:
        favorite_ids.append(id)

    request.session["favorites"] = favorite_ids

    return redirect("favorites")



def remove_favorite(request, id):
    favorite_ids = request.session.get("favorites", [])

    if id in favorite_ids:
        favorite_ids.remove(id)

    request.session["favorites"] = favorite_ids

    return redirect("favorites")









def favorites(request):
    favorite_ids = request.session.get("favorites", [])

    favorite_resources = [
        resource
        for resource in resources
        if resource["id"] in favorite_ids
    ]

    context = {
        "resources": favorite_resources,
        "theme": get_theme(request),
    }

    return render(request, "core/favorites.html", context)


def preferences(request):
    theme = request.COOKIES.get("theme", "light")

    if theme not in ["light", "dark"]:
        theme = "light"

    if request.GET.get("theme") in ["light", "dark"]:
        theme = request.GET.get("theme")

        response = render(
            request,
            "core/preferences.html",
            {"theme": theme}
        )

        response.set_cookie("theme", theme)

        return response

    return render(
        request,
        "core/preferences.html",
        {"theme": theme}
    )




def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST, request.FILES)

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            rating = form.cleaned_data["rating"]

            return redirect("feedback_thanks")
    else:
        form = FeedbackForm()

    context = {
        "form": form,
        "theme": get_theme(request),
    }

    return render(request, "core/feedback.html", context)


def feedback_thanks(request):
    context = {
        "theme": get_theme(request),
    }

    return render(request, "core/feedback_thanks.html", context)