# StudyHub

StudyHub is a Django-based learning resources website built for the Unit
4 Project. It provides a simple space to explore learning resources,
view resource details, save favorites, customize the site theme, and
submit feedback.

## Project Structure

``` text
studyhub_project/
├── manage.py
├── studyhub_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── core/
│   ├── urls.py
│   ├── views.py
│   ├── forms.py
│   ├── models.py
│   └── templates/
│       └── core/
│           ├── home.html
│           ├── resource_list.html
│           ├── resource_detail.html
│           ├── favorites.html
│           ├── preferences.html
│           ├── feedback.html
│           └── feedback_thanks.html
├── templates/
│   ├── base.html
│   └── 404.html
├── static/
│   ├── css/
│   │   ├── base.css
│   │   ├── light.css
│   │   └── dark.css
│   └── images/
├── media/
├── db.sqlite3
└── requirements.txt
```

## URLs and Views

The project uses app-level routing through `core/urls.py`.

  ----------------------------------------------------------------------------------------
  URL                                      View                    Purpose
  ---------------------------------------- ----------------------- -----------------------
  `/`                                      `home`                  Displays the StudyHub
                                                                   home page

  `/resources/`                            `resource_list`         Displays all learning
                                                                   resources

  `/resources/<int:id>/`                   `resource_detail`       Displays one resource
                                                                   using its integer ID

  `/resources/<int:id>/favorite/`          `add_favorite`          Adds a resource to the
                                                                   session favorites

  `/resources/<int:id>/remove-favorite/`   `remove_favorite`       Removes a resource from
                                                                   the session favorites

  `/favorites/`                            `favorites`             Displays saved favorite
                                                                   resources

  `/preferences/`                          `preferences`           Allows the user to
                                                                   choose a light or dark
                                                                   theme

  `/feedback/`                             `feedback`              Displays and processes
                                                                   the feedback form

  `/feedback/thanks/`                      `feedback_thanks`       Displays the successful
                                                                   feedback submission
                                                                   page

  `/admin/`                                Django admin            Django's built-in
                                                                   administration route
  ----------------------------------------------------------------------------------------

Resource details also support the query parameter `tab`, for example:

``` text
/resources/1/?tab=details
```

The `tab` value changes the content displayed on the resource detail
page.

Invalid resource IDs are handled with a custom 404 response.

## Templates

The project uses Django template inheritance through a shared
`base.html`.

`base.html` contains the shared:

-   Navigation
-   Site logo
-   Main content block
-   Footer
-   Static CSS loading
-   Theme class

Individual pages extend the base template with:

``` django
{% extends "base.html" %}
```

Named URLs are used with Django's `{% url %}` tag for internal
navigation.

## Static Files

Static files are stored in the `static/` directory.

``` text
static/
├── css/
│   ├── base.css
│   ├── light.css
│   └── dark.css
└── images/
```

The project uses Django's static-file system with:

``` django
{% load static %}
```

and:

``` django
{% static '...' %}
```

CSS files are loaded from `base.html`, while page-specific images use
Django static paths.

## Cookies

StudyHub uses a cookie to remember the user's selected theme.

The theme is read from:

``` python
request.COOKIES.get("theme", "light")
```

Only `light` and `dark` are accepted. If the cookie is missing or
contains an invalid value, the site defaults to the light theme.

When the user selects a theme from the Preferences page, the response
stores the choice using:

``` python
response.set_cookie("theme", theme)
```

This allows the selected theme to remain active while navigating between
pages.

## Sessions and Favorites

StudyHub uses Django sessions to store favorite resource IDs.

Favorites are read from:

``` python
request.session.get("favorites", [])
```

When a resource is added, its ID is stored in the session. The project
checks whether the ID already exists before adding it, preventing
duplicate favorites.

Favorites therefore remain available between requests without requiring
a database model for resources.

Users can also remove a resource from their favorites.

## Forms and Validation

The feedback page uses a Django `forms.Form` called `FeedbackForm`.

The form contains:

-   `name` --- required text field
-   `email` --- required email field
-   `message` --- required text field with a minimum length of 10
    characters
-   `rating` --- optional integer from 1 to 5
-   `screenshot` --- optional image upload

On a POST request, the form is bound with the submitted data and
validated using:

``` python
form.is_valid()
```

Validated values are accessed through:

``` python
form.cleaned_data
```

Validation errors are displayed on the feedback page when the submitted
data is invalid.

The form also includes Django's CSRF protection:

``` django
{% csrf_token %}
```

After a successful submission, the user is redirected to:

``` text
/feedback/thanks/
```

This follows the POST/Redirect/GET pattern.

The optional screenshot is accepted by the form for issue reporting, but
it is not stored permanently by the application.

## 404 Handling

The resource detail view checks whether the requested resource ID
exists.

If no matching resource is found, Django raises:

``` python
Http404("Resource not found")
```

The project also provides a custom `404.html` page that extends the
shared `base.html`.

## Known Limitations

-   Learning resources are stored in Python data structures rather than
    a database.
-   Favorites are session-based and are associated with the current
    browser session.
-   Feedback submissions are validated and redirected successfully, but
    feedback is not stored in a database.
-   Optional feedback screenshots are accepted by the form but are not
    permanently stored.
-   The project is intended as a Unit 4 learning project rather than a
    production application.

## Future Improvements

Possible future improvements include:

-   Storing resources in a database using Django models.
-   Persisting feedback submissions in a database.
-   Adding user authentication and accounts.
-   Adding search and filtering for resources.
-   Adding persistent user-specific favorites for authenticated users.
-   Improving accessibility and responsive behavior for additional
    screen sizes.

## Screenshots

The required project screenshots are provided separately as part of the
project deliverables.

The screenshot set includes:

1.  Home page
2.  Resource list
3.  Resource detail
4.  Favorites page
5.  Preferences page
6.  Light theme
7.  Dark theme
8.  Feedback form with validation errors
9.  Successful feedback submission
