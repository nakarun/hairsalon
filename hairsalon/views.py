from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from .models import News


# Create your views here.

class TopView(TemplateView):
    template_name = 'hairsalon/top.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = News.objects.order_by('-published')
        context['news'] = news
        context['current_menu_item'] = 'top'
        return context


class NewsDetailView(DetailView):
    template = 'hairsalon/news_detail.html'
    model = News

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_menu_item'] = 'news'
        return context


class MapView(TemplateView):
    template_name = 'hairsalon/map.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_menu_item'] = 'map'
        return context
