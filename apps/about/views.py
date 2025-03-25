from django.shortcuts import render
from django.views.generic import TemplateView
from apps.about.models import About, Team, Award, Need, Title, Contact

class AboutView(TemplateView):
    template_name = 'about.html'
    model = About

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about_all"] = About.objects.all()
        context["about_id"] = About.objects.latest("id")
        context['team_all'] = Team.objects.all()
        context["award_all"] = Award.objects.all()
        context["title_id"] = Title.objects.latest("id")
        context["need_all"] = Need.objects.all()
        context["contact_id"] = Contact.objects.latest("id")
        return context
