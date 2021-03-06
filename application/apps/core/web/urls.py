from django.urls import path

from . import views

# Register your urls here

urlpatterns = [
    path("", views.HomePageView.as_view(), name='home'),
    path("mailing", views.MailingPageView.as_view(), name='mailing'),
    path("users", views.UsersPageView.as_view(), name='users'),
]

# To register this URLS
# path("core/", include("apps.core.web.urls"))
