from django.shortcuts import render
from django.views.generic import TemplateView

from apps.about.models import About
# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'
    model = About
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about_all"] = About.objects.all()
        context["about_id"] = About.objects.latest("id")
        return context