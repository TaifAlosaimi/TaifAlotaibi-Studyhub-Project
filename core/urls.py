from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("resources/", views.resource_list, name="resource_list"),
    path("resources/<int:id>/", views.resource_detail, name="resource_detail"),
    path("resources/<int:id>/favorite/", views.add_favorite, name="add_favorite"),
    path(
    "resources/<int:id>/remove-favorite/",
    views.remove_favorite,
    name="remove_favorite",
    ),
    path("favorites/", views.favorites, name="favorites"),
    path("preferences/", views.preferences, name="preferences"),
    path("feedback/", views.feedback, name="feedback"),
    path("feedback/thanks/", views.feedback_thanks, name="feedback_thanks"),
]