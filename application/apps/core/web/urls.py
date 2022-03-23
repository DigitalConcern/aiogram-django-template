from django.urls import path

from . import views

# Register your urls here

urlpatterns = [
    path("", views.HomePageView.as_view(), name='home'),
    path("users/", views.UsersPageView.as_view(), name='users'),
]

# To register this URLS
# path("core/", include("apps.core.web.urls"))
