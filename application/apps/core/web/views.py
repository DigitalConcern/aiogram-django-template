from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
import asyncio

from ..models import User
from . import forms
from ..services import mailing


class HomePageView(TemplateView):
    template_name = 'home.html'


class UsersPageView(TemplateView):
    template_name = 'users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context


class MailingPageView(CreateView):
    template_name = 'mailing.html'
    form_class = forms.CommentForm
    success_url = reverse_lazy('home')

    async def get_success_url(self) -> str:
        text = self.request.POST.get('text')
        await mailing(text)
        return await super().get_success_url()

# async def simple_view(request: HttpRequest) -> HttpResponse:
#     return HttpResponse('Hello from "Core" app!')
