# from django.http import HttpRequest, HttpResponse
# from django.shortcuts import render
from django.views.generic import TemplateView
from django.core import serializers
from django.template.context import RequestContext, Context
from ..models import User


class HomePageView(TemplateView):
    template_name = 'home.html'


class UsersPageView(TemplateView):
    template_name = 'users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context


class MailingPageView(TemplateView):
    template_name = 'mailing.html'


# async def simple_view(request: HttpRequest) -> HttpResponse:
#     return HttpResponse('Hello from "Core" app!')
