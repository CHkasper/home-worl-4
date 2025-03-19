from django.shortcuts import render
from django.views.generic import TemplateView

from apps.settings.models import Settings, Text

# Create your views here.
# def index(request):
#     return render(request, 'index.html', locals())

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings_id'] = Settings.objects.latest("id")
        context['text_all'] = Text.objects.all()
        return context