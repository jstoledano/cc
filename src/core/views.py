"Vistas globales para el toolbox."
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """Vista de inicio."""
    template_name = 'index.html'
